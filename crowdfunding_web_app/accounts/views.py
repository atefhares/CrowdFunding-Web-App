from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import UserProfile
import re

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

def validate_string(name_field):
    if name_field == '':
        return True
    else:
        return False

def validate_password(password_field):
    PASS_REJEX = re.compile(r"^.{8,}$")
    if not PASS_REJEX.match(password_field):
        return True
    else:
        return False

def validate_email(email_field):
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if not EMAIL_REGEX.match(email_field):
        return True
    else:
        return False
def  validate_mobile_phone(phone_number):
    PHONE_REJEX = re.compile(r"^01[012][0-9]{8}")
    if not PHONE_REJEX.match(phone_number):
        return True
    else:
        return False

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        validate_string(first_name)
        if validate_string(first_name):
            messages.error(request, "First Name Is Required")

        last_name = request.POST['last_name']
        validate_string(last_name)
        if validate_string(last_name):
            messages.error(request, "Last Name Is Required")

        email = request.POST['email']
        validate_email(email)
        if validate_email == True:
            messages.error(request, "Invalid Email Format:example@domain.com")

        phone_number = request.POST['phone_number']
        validate_mobile_phone(phone_number)
        if validate_mobile_phone(phone_number):
            messages.error(request, "Phone Number Must Be 11 digits starts with 010 or 011 or 012")

        birth_date = request.POST['birth_date']

        password = request.POST['password']
        validate_password(password)
        if validate_password(password):
            messages.error(request, "Password Must Be At Least 8 Character")
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, "This Email already exists")
                return redirect('register')
            elif not validate_email(email) and not validate_mobile_phone(phone_number) and not validate_string(first_name) and not validate_string(last_name) and not validate_password(password):
                profile = UserProfile(
                    phone_number=phone_number,
                    birth_date=birth_date 
                    )
                user = User.objects.create_user(
                    username=email,
                    first_name=first_name,
                    email=email,
                    password=password,
                    last_name=last_name
                    )
                
                profile.user = user
                profile.save()
                messages.success(request,'Registered, Successfully! ')
                return redirect('login') 
        else:
            messages.error(request, "Passwords don't match")
            return redirect('register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['login_email']
        password = request.POST['login_password']
        

        user = auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"you are logged in!")
            return render(request, 'login.html')
        else:
            messages.error(request,"Invalid Credentials")
            return render(request, 'login.html')
        
    else:
        return render(request, 'login.html')

# def logout(request):
#     return redirect(request, 'acounts/index.html')

