from django.shortcuts import render
from infomun.models import Municipio
from infomun.models import Documento
from django.db.models import Q


# Create your views here.
def municipio_detail(request, id='015'):
    municipios = Municipio.objects.exclude(cve_mun='000').order_by('nom_mun_corto').values()
    municipio = Municipio.objects.get(id=id)
    docs1 = Documento.objects.filter(seccion=1).filter(Q(municipio__id=id) | Q(municipio__cve_mun='000')).order_by('posicion').values()
    docs2 = Documento.objects.filter(seccion=2).filter(Q(municipio__id=id) | Q(municipio__cve_mun='000')).order_by('posicion').values()
    docs3 = Documento.objects.filter(seccion=3).filter(Q(municipio__id=id) | Q(municipio__cve_mun='000')).order_by('posicion').values()
    docs4 = Documento.objects.filter(seccion=4).filter(Q(municipio__id=id) | Q(municipio__cve_mun='000')).order_by('posicion').values()
    docs5 = Documento.objects.filter(seccion=5).filter(Q(municipio__id=id) | Q(municipio__cve_mun='000')).order_by('posicion').values()
    context = {
        'municipios': municipios,
        'municipio': municipio,
        'docs1': docs1,
        'docs2': docs2,
        'docs3': docs3,
        'docs4': docs4,
        'docs5': docs5
    }
    return render(request, 'municipio_detail.html', context)
