# Generated by Django 4.1.5 on 2023-01-26 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infomun', '0009_documento_delete_documento_comun_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'ordering': ['municipio', 'seccion', 'posicion']},
        ),
    ]
