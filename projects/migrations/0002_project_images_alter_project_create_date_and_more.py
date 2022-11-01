# Generated by Django 4.1.2 on 2022-10-30 12:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="images",
            field=models.FileField(default=258, upload_to=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="project",
            name="create_date",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(2022, 10, 30, 12, 34, 0, 359346)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 29, 12, 34, 0, 359332)
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="start_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 30, 12, 34, 0, 359322)
            ),
        ),
    ]
