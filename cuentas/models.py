from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    """Usuario del sistema. El rol determina qué puede hacer."""

    class Rol(models.TextChoices):
        ESTUDIANTE = 'estudiante', 'Estudiante'
        EMPRESA = 'empresa', 'Empresa'
        ADMIN = 'admin', 'Administrador UTC'

    rol = models.CharField(max_length=20, choices=Rol.choices, default=Rol.ESTUDIANTE)

    def __str__(self):
        return f'{self.username} ({self.get_rol_display()})'
