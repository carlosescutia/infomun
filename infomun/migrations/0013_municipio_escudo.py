# Generated by Django 4.1.5 on 2023-01-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomun', '0012_remove_municipio_escudo'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipio',
            name='escudo',
            field=models.FilePathField(blank=True, default=None, null=True),
        ),
    ]
