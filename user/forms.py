from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.forms import ModelForm

from user.models import Profile


#Registeration Form
class RegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email = forms.EmailField(required=True)
	#profile_pic = forms.ImageField()
	#phone_regex = RegexValidator(regex= r'^01[0-2][0-9]{8}$', message="Phone number must be entered in the format: '01*********'. Up to 11 digits allowed.")
	#mobile = forms.CharField(max_length=11)  # Validators should be a list
	class Meta:
		model = User
		fields = ("username","first_name","last_name","email","password1", "password2")

class UserProfileCreate(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['profile_pic','mobile_number']

class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', "first_name","last_name"]

class UpdateProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['birthday', 'country','social_profile','profile_pic','mobile_number']
