# Generated by Django 4.1.5 on 2023-01-20 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='cve_mun',
            field=models.CharField(blank=True, default=None, max_length=3, null=True),
        ),
    ]
