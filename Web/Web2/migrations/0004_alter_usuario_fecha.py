# Generated by Django 4.1.1 on 2022-10-02 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web2', '0003_alter_usuario_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha'),
        ),
    ]