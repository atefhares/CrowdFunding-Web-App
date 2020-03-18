from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    return render(request, 'register.html')



def login(request):
    return render(request, 'login.html')


# def logout(request):
#     return redirect(request, 'acounts/index.html')