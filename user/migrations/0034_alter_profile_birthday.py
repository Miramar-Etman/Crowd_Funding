# Generated by Django 4.1.2 on 2022-11-01 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0033_alter_profile_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="birthday",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 11, 1, 15, 47, 28, 455193)
            ),
        ),
    ]
