# Generated by Django 3.2.5 on 2021-07-21 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_arbustos_tierradehojas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('correo', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Correo')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre')),
            ],
        ),
    ]
