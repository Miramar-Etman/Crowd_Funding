# Generated by Django 4.1.2 on 2022-11-02 23:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0037_alter_profile_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="birthday",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 2, 23, 44, 41, 631412)
            ),
        ),
    ]