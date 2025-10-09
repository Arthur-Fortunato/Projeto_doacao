from django.shortcuts import render

def load_home_page(request):
    return render(request, "home/home.html")