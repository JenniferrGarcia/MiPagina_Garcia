# Generated by Django 5.2 on 2025-04-16 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_usuario_rename_project_mascota_delete_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.CharField(default='Desconocida', max_length=200),
        ),
        migrations.AddField(
            model_name='mascota',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
