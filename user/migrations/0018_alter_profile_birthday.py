# Generated by Django 4.1.2 on 2022-10-31 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0017_alter_profile_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="birthday",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 10, 31, 19, 32, 25, 652434)
            ),
        ),
    ]
