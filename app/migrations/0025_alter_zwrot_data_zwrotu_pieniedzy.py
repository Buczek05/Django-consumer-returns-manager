# Generated by Django 4.0.5 on 2022-06-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_zwrot_data_zwrotu_pieniedzy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zwrot',
            name='data_zwrotu_pieniedzy',
            field=models.DateField(blank=True, null=True),
        ),
    ]
