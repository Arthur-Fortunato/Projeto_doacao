from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def load_home_page(request):
    return render(request, "home/home.html")