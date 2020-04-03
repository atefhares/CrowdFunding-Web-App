from datetime import timedelta
import datetime
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import UserProfile
import re
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.template.loader import get_template
from django.utils import timezone
import random
import string
import pytz


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


def validate_mobile_phone(phone_number):
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
        if validate_email(email):
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
                if birth_date == '':
                    profile = UserProfile(
                        phone_number=phone_number,
                        key = random_string_generator(size=45), 
                        )
                else:
                        profile = UserProfile(
                        phone_number=phone_number,
                        birth_date= birth_date,
                        key = random_string_generator(size=45), 
                        )
                user = User.objects.create_user(
                    username=first_name,
                    first_name=first_name,
                    email=email,
                    password=password,
                    last_name=last_name,

                )
                user.active = False
                profile.time_stamp = datetime.datetime.now()
                profile.expires = profile.time_stamp + datetime.timedelta(hours=24)

                profile.user = user

                if send_activation(user, profile):
                    profile.save()

                messages.success(request, '<strong>Success</strong><br>Registered, Successfully!',
                                 extra_tags='contains_html')
                messages.info(request,
                              """<strong>Info</strong><br>
                              <p>
                              An activation mail is sent to you.
                              once you verify your mail, You can login.<br>
                              Note: This mail will be expired after 24 hours.</p>
                              """,
                              extra_tags='contains_html'
                              )
                # return render(request, 'RegisteredSucceccfully.html', context)
                return redirect('login')
        else:
            messages.error(request, "Passwords don't match")
            return redirect('register')
    return render(request, 'accounts/register.html')


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def send_activation(user, profile):  # responsoble for sending the mail
    is_sent = False

    # send_email(subject,message,from_email,recipient_list,html_message)
    context = {
        'key': profile.key,
        'email': user.email,
        'username': user.first_name
    }
    html_ = get_template("accounts/verify.html").render(context)
    txt_ = get_template("accounts/verify.txt").render(context)
    mail_subject = 'Verification Mail'
    mail_sender = 'crowdfundingwebapp@gmail.com'
    mail_reciever = [user.email]
    send_email = send_mail(
        mail_subject,
        txt_,
        mail_sender,
        mail_reciever,
        html_message=html_,
    )
    is_sent = True
    return is_sent


def activate(request, key):
    try:
        user_profile = UserProfile.objects.get(key=key)
    except(UserProfile.DoesNotExist, OverflowError, ValueError, TypeError):
        user_profile = None
        return render(request, 'accounts/verify.html')
    utc = pytz.UTC
    now = datetime.datetime.now().replace(tzinfo=utc)
    expires = user_profile.expires.replace(tzinfo=utc)

    if user_profile is not None and now <= expires:
        if not user_profile.once_activation:
            user_profile.once_activation = True
            user_profile.is_active = True
            user_profile.save()
            messages.success(request, "Your mail is successfully activated.")
            return render(request, 'accounts/login.html')
        elif user_profile.once_activation == True and user_profile.is_active == True:
            messages.info(request, "Your email is already activated")
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/verify.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['login_email']
        password = request.POST['login_password']

        email_validation_result = validate_email(email)
        if email_validation_result:
            messages.error(request, "Invalid Email")

        password_validation_result = validate_password(password)
        if password_validation_result:
            messages.error(request, "Password Must Be More Than Or Equal 8 Characters")
        user = auth.authenticate(username=email, password=password)

        try:
            user_profie = UserProfile.objects.get(user__email=email)
        except(UserProfile.DoesNotExist, OverflowError, ValueError, TypeError):
            messages.error(request, "Invalid Credentials")
            return render(request, 'accounts/login.html')
        if user is not None and user_profie.is_active == True:
            auth.login(request, user)
            return redirect('/')
        elif user is not None and user_profie.is_active == False:
            messages.error(request, "This email is not activated yet, If you activation email is expired ClickHere")
            return render(request, 'accounts/login.html')
        else:
            messages.error(request, "Invalid Credentials")
            return render(request, 'accounts/login.html')

    else:
        return render(request, 'accounts/login.html')

# def logout(request):
#     return redirect(request, 'acounts/index.html')
