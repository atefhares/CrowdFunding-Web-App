# from django.shortcuts import render
from login_registration.models import User, Country
from django.shortcuts import render
users=[
    { 'firstname':'Esraa',
      'lastname':'salah',
      'email':'esraa@gmail.com',
      'phone':'26598544',
      'birthdate':'2-8-1996,'

    },
    {'firstname': 'Nehal',
     'lastname': 'khaled',
     'email': 'nehal@gmail.com',
     'phone': '26598544',
     'birthdate': '7-8-1992,'

     }
]

def view_profile(request,id):
    context={
        'users':users
    }

    return render(request, "user_profile/pro.html",context)
