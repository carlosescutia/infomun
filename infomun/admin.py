from django.contrib import admin
from .models import Municipio
from .models import Documento

# Register your models here.
admin.site.register(Municipio)


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_filter = ('municipio', 'posicion')
