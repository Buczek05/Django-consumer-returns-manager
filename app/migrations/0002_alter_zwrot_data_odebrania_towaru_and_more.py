# Generated by Django 4.0.5 on 2022-06-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zwrot',
            name='data_odebrania_towaru',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='zwrot',
            name='dowod_zakupu',
            field=models.BooleanField(),
        ),
    ]
