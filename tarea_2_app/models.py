from django.db import models

# Create your models here.


class Concesion(models.Model):
    id = models.IntegerField(unique=True, primary_key=True) #n_concesion
    tipo_de_concesion = models.CharField()
    comuna = models.CharField()
    lugar = models.CharField()
    n_rs_ds = models.CharField()
    tipo_tramite = models.CharField()
    concesionario = models.CharField()
    tipo_vigencia = models.CharField()

    #objeto
    #sector geografico
    #data region
    #fecha vencimiento
    #Fecha Última Actualización Sector
    #Fecha Última Actualización Imagen Decreto
    #Fecha Última Actualización Imagen Mapa	