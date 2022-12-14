# Generated by Django 4.1.2 on 2022-10-31 23:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0026_alter_project_create_date_alter_project_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="create_date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2022, 10, 31, 23, 37, 38, 37449)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 30, 23, 37, 38, 37442)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 31, 23, 37, 38, 37434)
            ),
        ),
        migrations.CreateModel(
            name="Donate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField()),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="donate",
                        to="projects.project",
                    ),
                ),
                (
                    "user_donated",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="donate",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
