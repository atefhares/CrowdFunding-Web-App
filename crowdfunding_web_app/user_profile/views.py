# from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import UserUpdateForm,ProfileUpdateForm,UserDeleteForm,ProfileDeleteForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from accounts.models import UserProfile,User,Country,CountryField

from django.urls import reverse

def profile(request):
    return render(request, 'user_profile/pro.html')

def edit_profile(request):
    print (request.user.email)
    if request.method =='POST':
        user_form=UserUpdateForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,
                                 request.FILES,
                                 instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')


    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
    context ={
        'u_form':user_form,
        'p_form':profile_form

    }
    return render(request, "user_profile/edit.html",context)

def deleteuser(request):
    if request.method == 'GET':
        return render(request, "user_profile/delete.html")

        # deleteform=UserDeleteForm(request.POST,instance=user)
        # deletepform=ProfileDeleteForm(request.POST,
        #                               request.FILES,
        #                               instance=request.user.userprofile
        #
        #                              )
    else:

        request.user.userprofile.delete()
        request.user.delete()

        messages.info(request, 'Your account has been deleted.')
        return redirect('/')







