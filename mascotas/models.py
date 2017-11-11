from django.db import models


class Mascota(models.Model):
    TIPOS = (
        ('canino', 'Canino'),
        ('felino', 'Felino'),
    )
    
    tipo = models.CharField(max_length=100, choices=TIPOS)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    pelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    edad = models.IntegerField()  
    tamanio = models.FloatField()
    descripcion = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='fotos/mascotas/')

    def __str__(self):
        return "%s (%s)" % (self.nombre, self.tipo)


class Estado(models.Model):
    mascota = models.ForeignKey('mascotas.Mascota', related_name='estados')
    estado = models.ForeignKey('TiposDeEstados', related_name='estados')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.estado 


class TiposDeEstados(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    


class Aviso(models.Model):
    mascota = models.ForeignKey('mascotas.Mascota', related_name='avisos')
    estado = models.ForeignKey('Estado', related_name='avisos')
    fecha_vencimiento = models.DateField()
    publicado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.mascota
