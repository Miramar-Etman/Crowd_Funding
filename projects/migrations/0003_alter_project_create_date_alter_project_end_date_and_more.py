# Generated by Django 4.1.2 on 2022-10-30 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_project_images_alter_project_create_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="create_date",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(2022, 10, 30, 13, 2, 42, 82247)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 29, 13, 2, 42, 82240)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 30, 13, 2, 42, 82230)
            ),
        ),
    ]
