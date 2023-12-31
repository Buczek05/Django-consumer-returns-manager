# Generated by Django 4.0.5 on 2022-06-22 08:51

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_zwrot_telefon'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zwrot',
            options={'verbose_name_plural': 'Zwroty'},
        ),
        migrations.AlterField(
            model_name='zwrot',
            name='data_odebrania_towaru',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='zwrot',
            name='telefon',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
