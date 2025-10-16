from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('doador', 'Doador'),
        ('receptor', 'Receptor'),
    ])

    def __str__(self):
        return f"{self.user.username} ({self.status})"
