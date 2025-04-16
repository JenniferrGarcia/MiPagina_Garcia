# Generated by Django 5.2 on 2025-04-16 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_task_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Project',
            new_name='Mascota',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
