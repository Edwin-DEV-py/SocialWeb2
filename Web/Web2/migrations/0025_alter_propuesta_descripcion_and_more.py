# Generated by Django 4.1.1 on 2022-10-16 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web2', '0024_alter_propuesta_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propuesta',
            name='Descripcion',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='propuesta',
            name='diapostivas',
            field=models.FileField(blank=True, null=True, upload_to='diapositivas/'),
        ),
        migrations.AlterField(
            model_name='propuesta',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]