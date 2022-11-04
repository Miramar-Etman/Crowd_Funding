# Generated by Django 4.1.2 on 2022-11-03 23:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0045_alter_commentreport_comment_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="images",
        ),
        migrations.AlterField(
            model_name="project",
            name="create_date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2022, 11, 3, 23, 37, 9, 581757)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 3, 23, 37, 9, 581750)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 3, 23, 37, 9, 581742)
            ),
        ),
        migrations.CreateModel(
            name="Photo",
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
                (
                    "image",
                    models.ImageField(
                        default="media/media/istockphoto-913374922-612x612.jpg",
                        null=True,
                        upload_to="",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="project",
                        to="projects.project",
                    ),
                ),
            ],
        ),
    ]