# Generated by Django 4.1.1 on 2022-10-12 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web2', '0013_universitario_lider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propuesta',
            name='diapostivas',
            field=models.FileField(upload_to='diapositivas'),
        ),
    ]