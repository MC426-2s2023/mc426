# Generated by Django 3.2.12 on 2023-11-26 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='registro_de_ocorrencia',
        ),
        migrations.DeleteModel(
            name='tipo_de_ocorrencia',
        ),
    ]
