# Generated by Django 5.0.3 on 2024-03-15 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['-name'], 'verbose_name': 'Mis Departamentos', 'verbose_name_plural': 'Areas de la Empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'sort_name')},
        ),
    ]
