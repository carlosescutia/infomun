# Generated by Django 4.1.5 on 2023-01-26 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomun', '0010_alter_documento_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='municipio',
            name='nom_pmd',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='panorama_sociodem',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='pmd',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='prg_gob',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='prg_gob2',
        ),
        migrations.AddField(
            model_name='municipio',
            name='escudo',
            field=models.FilePathField(blank=True, default=None, null=True, path='/img/escudos'),
        ),
    ]
