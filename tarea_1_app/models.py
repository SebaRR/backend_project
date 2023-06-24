from django.db import models

# Create your models here.

class Jurisprudencia(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)
    tipoCausa = models.CharField()
    rol = models.CharField()
    caratula = models.CharField()
    nombreProyecto = models.CharField()
    fechaSentencia = models.DateField()
    descriptores = models.CharField()
    linkSentencia = models.CharField()
    urlSentencia = models.CharField()
    activo = models.BooleanField()
    tribunal = models.CharField()
    #valores separados en una tabla a parte
    tipo = models.CharField()
    relacionada = models.CharField(null=True, blank=True)
    visitas = models.IntegerField()

    def __str__(self):
        return self.nombreProyecto


class ValoresJurisprudencia(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)
    idParametro = models.IntegerField()
    idItemlista = models.IntegerField(null=True, blank=True)
    valor = models.CharField(null=True, blank=True)
    parametro = models.CharField()
    item = models.CharField(null=True, blank=True)

    jurisprudencia = models.ForeignKey(Jurisprudencia, on_delete=models.CASCADE, null=True, blank=True)












