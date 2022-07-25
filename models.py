from django.db import models

# Create your models here.

from tkinter import Widget

class Cotizantes(models.Model):
    ente = models.CharField(max_length=12, default="", null=False)
    periodo = models.CharField(max_length=6, default="", null=False)
    ficha = models.IntegerField(default=0)
    nombre = models.CharField(max_length=40, default="", null=False)
    dni = models.IntegerField(default=0)
    cuil = models.IntegerField(default=0)
    repa = models.IntegerField(default=0)
    loca = models.IntegerField(default=0)
    importe = models.FloatField(default=0)
    detalle = models.CharField(max_length=20, default="")
    afiliado = models.IntegerField(default=0)
    
    def __str__(self):
        return f'Cotizante: {self.nombre} -- DNI: {self.dni} -- Repa: {self.repa} -- Loca: {self.loca} -- Importe: {self.importe}'