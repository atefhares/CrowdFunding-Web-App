from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from admins.models import Admin, FeaturedProject


def index(request):
    staff_picks = get_staff_picks()
    user = {'is_signedin': request.user.is_authenticated}
    context = {'staff_picks': staff_picks, 'user': user}

    return render(request, 'homepage/index.html', context=context)


def get_staff_picks():
    staff_picks = FeaturedProject.objects.order_by('date_featured').first()
    return staff_picks


