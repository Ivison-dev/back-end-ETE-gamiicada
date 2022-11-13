# Generated by Django 4.1.2 on 2022-10-31 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, primary_key=True, serialize=False)),
                ('senha', models.CharField(max_length=100)),
                ('pontos_conhecimento', models.PositiveIntegerField()),
            ],
        ),
    ]
