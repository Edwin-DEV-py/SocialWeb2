# Generated by Django 4.1.1 on 2022-10-16 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web2', '0027_comentario_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]