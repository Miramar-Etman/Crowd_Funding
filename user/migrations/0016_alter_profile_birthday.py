# Generated by Django 4.1.2 on 2022-10-31 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0015_alter_profile_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="birthday",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 31, 17, 8, 59, 100392)
            ),
        ),
    ]
