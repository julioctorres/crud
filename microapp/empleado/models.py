from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
 
class empleado(models.Model):
    codigo = models.IntegerField()
    nif = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido_1 = models.CharField(max_length=20)
    apellid_2 = models.CharField(max_length=20)
    codigo_departamento = models.IntegerField()
