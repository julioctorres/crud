from django.db import models

# Create your models here.
class departamento(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=20)
    presupuesto = models.FloatField(null=True)
