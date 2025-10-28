from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def load_home_page(request):
    return render(request, "home/home.html")