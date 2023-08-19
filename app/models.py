from dataclasses import fields
from email.policy import default
from django.db import models
from django import forms
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
import datetime
from django import forms


custom_widgets = [forms.CheckboxInput, forms.RadioSelect]
# Create your models here.
class Zwrot(models.Model):
    class Meta:
        verbose_name_plural = "Zwroty"

    imie = models.CharField(max_length=256)
    nazwisko = models.CharField(max_length=256)
    telefon = PhoneNumberField(blank=True)
    towar = models.TextField()
    paragon = models.BooleanField()
    faktura = models.BooleanField()
    cena_zakupu = models.FloatField(blank=True, null=True)
    dane_do_zwrotu = models.BooleanField()
    powod_zwrotu = models.CharField(blank=True, max_length=256, null=True)
    data_odebrania_towaru = models.DateField(default=datetime.date.today)
    numer_konta = models.CharField(blank=True, max_length=256)
    data_zwrotu_pieniedzy = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    def get_absolute_url(self):
        return reverse("app:view", kwargs={"pk": self.pk})
