from django.db import models

from aplications.departamentos.models import Departamento

class Habilidades (models.Model):
    habilidad= models.CharField('Habilidades', max_length=50)

    def __str__(self):
        return str (self.id) +'-'+ self.habilidad

# Create your models here.
class Empleado(models.Model):
    #Contador
    #Administrador
    #Economista
    #Otro
    JOB_CHOICES= (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('0', 'Economista'),
        ('0', 'Otro'),
    )

    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Puesto Trabajo', max_length=50, choices=JOB_CHOICES)
    #imagen = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, default=1)
    habilidades=models.ManyToManyField(Habilidades)

    def __str__(self):
        return self.first_name


