# Generated by Django 4.1.2 on 2022-11-01 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autentificacao', '0002_alter_usuario_pontos_conhecimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='pontos_conhecimento',
            field=models.PositiveIntegerField(),
        ),
    ]
