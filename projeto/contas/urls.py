from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('redefinir_senha/', auth_views.PasswordResetView.as_view(template_name = 'contas/redefinicao.html'), name='redefinir_senha'),
    path('redefinir-senha/enviado/', auth_views.PasswordResetDoneView.as_view(template_name='contas/redefinir_senha_enviado.html'), name='password_reset_done'),
    path('redefinir-senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='contas/nova_senha.html'), name='password_reset_confirm'),
    path('redefinir-senha/concluido/', auth_views.PasswordResetCompleteView.as_view(template_name='contas/redefinir_sucesso.html'), name='password_reset_complete'),
]
