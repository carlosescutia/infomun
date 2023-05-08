from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Municipio(models.Model):
    cve_mun = models.CharField(max_length=3, default=None, blank=True, null=True)
    nom_mun_corto = models.CharField(max_length=50, default=None, blank=True, null=True)
    nom_mun_largo = models.CharField(max_length=200, default=None, blank=True, null=True)
    presidente = models.CharField(max_length=80, default=None, blank=True, null=True)
    poblacion = models.IntegerField(default=None, blank=True, null=True)
    localidades = models.IntegerField(default=None, blank=True, null=True)
    superficie = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)
    escudo = models.ImageField(upload_to='img/escudos', default=None, blank=True, null=True)

    @property
    def escudo_url(self):
        if self.escudo and hasattr(self.escudo, 'url'):
            return self.escudo.url

    def __str__(self):
        return f"{self.cve_mun} {self.nom_mun_corto}"

    class Meta:
        ordering = ['cve_mun']


class Documento(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    etiqueta = models.TextField(default=None, blank=True, null=True)
    url = models.TextField(default=None, blank=True, null=True)
    archivo = models.FileField(upload_to='docs', default=None, blank=True, null=True)
    seccion = models.IntegerField(default=None, blank=True, null=True)
    posicion = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.municipio.cve_mun} {self.municipio.nom_mun_corto} - {self.seccion} {self.posicion} - {self.etiqueta}"

    class Meta:
        ordering = ['municipio', 'seccion', 'posicion']
