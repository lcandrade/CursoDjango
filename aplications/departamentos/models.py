from django.db import models

# Create your models here.
class Departamento(models.Model):
    name= models.CharField('Nombre', max_length=38, blank=True)
    sort_name= models.CharField('Nombre Corto', max_length=50, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return str (self.id) +'-' + self.name + '-' + self.sort_name

    #uso de clase Meta
    class Meta:
        verbose_name='Mis Departamentos'
        verbose_name_plural='Areas de la Empresa'
        ordering=['-name']
        unique_together= ('name','sort_name')