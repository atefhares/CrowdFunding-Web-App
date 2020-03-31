# from django.shortcuts import render
from login_registration.models import User, Country
from django.shortcuts import render,redirect
from .forms import UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.urls import reverse


def view_profile(request,id):
    if request.method =='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,
                                 request.FILES,
                                 instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            # return redirect('')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    context ={
        'u_form':u_form,
        'p_form':p_form

    }
    return render(request, "user_profile/pro.html",context)
