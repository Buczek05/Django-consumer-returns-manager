# Generated by Django 4.0.5 on 2022-06-27 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_zwrot_data_zwrotu_pieniedzy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zwrot',
            name='data_zwrotu_pieniedzy',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
