from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import BootstrapRegisterForm
from datetime import datetime
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Task
import json


class TodoView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest):
        tasks = Task.objects.filter(user=request.user)
        return render(request, "manager/todo.html", {"tasks": tasks})

    def post(self, request: HttpRequest):
        """Создать задачу"""
        try:
            data = json.loads(request.body)  # Десериализация JSON данных
            note = data.get("note", "")
            if note:
                Task(title=note, user=request.user).save()
            # Здесь вы можете обработать полученную заметку
            return JsonResponse({"status": "success"})
        except ValueError as ve:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    def put(self, request: HttpRequest):
        """Обновить задачу"""
        try:
            data = json.loads(request.body)  # Десериализация JSON данных
            title, date, task_id = (
                data.get("title"),
                data.get("date"),
                data.get("taskId"),
            )
            task = Task.objects.get(id=task_id)
            if title:
                task.title = title
            if date:
                task.before_at = date

            task.save()
            return JsonResponse({"status": "success"})
        except ValueError as ve:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    def patch(self, request: HttpRequest):
        """Частичное обновление: задача выполнена"""
        try:
            data = json.loads(request.body)  # Десериализация JSON данных
            done = data.get("done")
            task_id = data.get("taskId")
            task = Task.objects.get(id=task_id)
            task.done = done
            task.save()
            return JsonResponse({"status": "success"})
        except ValueError as ve:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    def delete(self, request: HttpRequest):
        """Удалить задачу"""
        try:
            data = json.loads(request.body)  # Десериализация JSON данных
            task_id = data.get("taskId")
            task = Task.objects.get(id=task_id)
            task.delete()
            return JsonResponse({"status": "success"})
        except ValueError as ve:
            return JsonResponse({"error": "Invalid JSON"}, status=400)


@login_required
def get_completed_tasks(request: HttpRequest):
    user = request.user
    tasks = Task.objects.filter(user=user, done=1)
    return render(request, "manager/completed_tasks.html", {"tasks": tasks})


def registration(request: HttpRequest):
    if request.method == "POST":
        regform = BootstrapRegisterForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()

            regform.save()

            return redirect(reverse("login"))
        else:
            messages.error(
                request,
                "Пароль слишком простой. Пожалуйста, используйте более сложный пароль.",
            )
    else:
        regform = BootstrapRegisterForm()
    return render(
        request,
        "registration/registration.html",
        {"regform": regform},
    )
