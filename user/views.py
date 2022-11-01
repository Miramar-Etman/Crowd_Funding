from datetime import datetime, timedelta
import pytz
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.shortcuts import  render, redirect
from gitdb.utils.encoding import force_text
from .forms import RegisterForm, UpdateUserForm, UpdateProfileForm, UserProfileCreate
from django.contrib.auth import login
from django.contrib import messages
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


################ REGISTER USER AND SEND EMAIL VERIFICATION LINK #########################
def register_user(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		profile_form = UserProfileCreate(request.POST)
		if form.is_valid() and profile_form.is_valid() :
			user = form.save(commit=False)
			profile= profile_form.save(commit=False)
			user.is_active = False
			user.save()
			user = User.objects.get(username=request.POST['username'])
			profile.user = user
			profile.save()
			messages.success(request, "Registration successful." )
			# to get the domain of the current site
			current_site = get_current_site(request)
			mail_subject = 'Activation link has been sent to your email id'
			message = render_to_string('user/acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
				mail_subject, message, to=[to_email]
			)
			email.send()
			return HttpResponse('Please confirm your email address to complete the registration')
		#login(request,user)
		else:
			messages.error(request, "Unsuccessful Registration. Invalid Information.")
			return render(request,"user/register.html",{"form":form,"profile":profile_form})
	else:
		form = RegisterForm()
		profile= UserProfileCreate()
		return render(request, "user/register.html", {"form":form,"profile":profile})

##################LOGIN##################
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None and user.is_active==True:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("user_profile")
			else:
				messages.error(request,"Invalid username or password,"
									   "Incase you havenot activated your account "
									   "please go back to your mail and activate before login")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="user/login.html", context={"login_form":form})

##############Profile#################
@login_required
def user_profile(request):
	user = request.user
	profile = request.user.profile
	context={"user":user,"profile":profile
			 }
	return render(request,"user/profile.html",context)

#############EMAIL-ACTIVATION WITH 24 HOURS EXPIRE LINK ########################
def activate(request, uidb64, token):
	User = get_user_model()
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	utc_now = datetime.utcnow()
	utc_now = utc_now.replace(tzinfo=pytz.utc)
	if user.date_joined > utc_now - timedelta(hours=24):
		if user is not None and account_activation_token.check_token(user, token):
			user.is_active = True
			user.save()
			return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	return HttpResponse('Activation link is invalid!')

#####################	EDIT PROFILE ##############
@login_required
def edit_profile(request):
	if request.method == 'POST':
		user_form = UpdateUserForm(request.POST, instance=request.user)
		profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Your profile is updated successfully')
			return redirect('edit_profile')
	else:
		user_form = UpdateUserForm(instance=request.user)
		profile_form = UpdateProfileForm(instance=request.user.profile)

	return render(request, 'user/edit.html', {'user_form': user_form, 'profile_form': profile_form})

#####################User LOGOUT###################
def log_out(request):
	logout(request)
	messages.success(request, "You Are Logged Out ......")
	return redirect('home')

###################DELETE ACCOUNT ##################
@login_required
def delete(request):
	if request.method == 'POST':
		request.user.delete()
		return redirect('home')
	else:
		return render(request, 'user/delete_confirm.html')
