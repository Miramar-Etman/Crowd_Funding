from datetime import datetime
import pytz
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    birthday = models.DateTimeField(default= datetime.now())
    country = models.CharField(max_length=2, choices=pytz.country_names.items())
    social_profile = models.URLField()
    mobile_number = models.CharField(max_length=11,validators=[RegexValidator(r'^01[0-2][0-9]{8}$', 'Egyptian Numbers only allowed')])
    profile_pic= models.ImageField(null=True,blank=True,upload_to='media/')

    def __str__(self):
        return str(self.user)