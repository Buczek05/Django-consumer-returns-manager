from django import forms
from app.models import Zwrot
from django.forms import ModelForm, TextInput


class Zwrot_forms(ModelForm):
    class Meta:
        model = Zwrot
        fields = [
            "imie",
            "nazwisko",
        ]
        widgets = {
            "imie": TextInput(
                attrs={
                    "class": "form-control bg-black text-white",
                    "style": "max-width: 300px;",
                    "placeholder": "imie",
                }
            ),
            "nazwisko": TextInput(
                attrs={
                    "class": "form-control bg-black text-white",
                    "style": "max-width: 300px;",
                    "placeholder": "nazwisko",
                }
            ),
        }
