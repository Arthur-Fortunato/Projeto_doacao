from django.contrib import admin
from django.urls import path, include
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('contas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('', include("home.urls"))
]
