from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    TIPOS = (
        ('vacunacion', 'Vacunacion'),
        ('castracion', 'Castracion'),
    )

    autor = models.ForeignKey(User)
    tipo = models.CharField(max_length=100, choices=TIPOS)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self):
        return self.titulo
    