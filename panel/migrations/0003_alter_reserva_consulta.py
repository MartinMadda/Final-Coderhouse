# Generated by Django 4.0.4 on 2022-11-10 01:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_alter_reserva_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='consulta',
            field=ckeditor.fields.RichTextField(default='Ingrese su consulta aquí'),
        ),
    ]
