# Generated by Django 4.1.2 on 2022-11-02 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0042_alter_project_create_date_alter_project_end_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="create_date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2022, 11, 2, 16, 42, 44, 717958)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 2, 16, 42, 44, 717951)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 2, 16, 42, 44, 717943)
            ),
        ),
    ]
