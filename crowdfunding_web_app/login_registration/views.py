from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    return render(request, 'login_registration/templates/register.html')



def login(request):
    return render(request, 'login_registration/templates/login.html')


# def logout(request):
#     return redirect(request, 'login_register/index.html')