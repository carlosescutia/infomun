from django.urls import path
from . import views

urlpatterns = [
    path("", views.municipio_detail, name="municipio_detail"),
    path("<str:id>/", views.municipio_detail, name="municipio_detail"),
]
