# Generated by Django 4.1.2 on 2022-10-30 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_alter_project_create_date_alter_project_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="create_date",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(2022, 10, 30, 13, 24, 0, 827386)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 29, 13, 24, 0, 827379)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 30, 13, 24, 0, 827368)
            ),
        ),
    ]
