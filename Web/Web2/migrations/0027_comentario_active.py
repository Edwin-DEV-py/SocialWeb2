# Generated by Django 4.1.1 on 2022-10-16 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web2', '0026_remove_propuesta_padre_alter_propuesta_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
