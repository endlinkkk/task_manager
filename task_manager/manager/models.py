from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название задачи")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания задачи"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Время изменения задачи"
    )
    before_at = models.DateField(
        verbose_name="Время на выполнение задачи",
        default=timezone.localdate() + timezone.timedelta(days=1),
        null=True,
        blank=True,
    )
    done = models.BooleanField(verbose_name="Задача выполнена", default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="tasks",
    )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
