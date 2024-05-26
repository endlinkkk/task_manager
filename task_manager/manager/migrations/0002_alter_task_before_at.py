# Generated by Django 5.0.6 on 2024-05-26 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="before_at",
            field=models.DateField(
                blank=True,
                default=datetime.date(2024, 5, 27),
                null=True,
                verbose_name="Время на выполнение задачи",
            ),
        ),
    ]