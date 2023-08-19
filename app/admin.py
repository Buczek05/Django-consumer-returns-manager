from django.contrib import admin
from app.models import Zwrot


class ZwrotAdmin(admin.ModelAdmin):
    fields = [
        "imie",
        "nazwisko",
        "telefon",
        "towar",
        "paragon",
        "faktura",
        "cena_zakupu",
        "dane_do_zwrotu",
        "powod_zwrotu",
        "numer_konta",
        "data_odebrania_towaru",
        'data_zwrotu_pieniedzy',
    ]

    search_fields = ["imie", "nazwisko", "telefon", "towar", "dane_do_zwrotu"]

    list_filter = ["paragon", "faktura", "dane_do_zwrotu", "data_odebrania_towaru", 'data_zwrotu_pieniedzy']

    list_display = [
        "imie",
        "nazwisko",
        "telefon",
        "towar",
        "paragon",
        "faktura",
        "cena_zakupu",
        "dane_do_zwrotu",
        "powod_zwrotu",
        "dane_do_zwrotu",
        "numer_konta",
        "data_odebrania_towaru",
        'data_zwrotu_pieniedzy',
    ]

    # list_editable = [
    #     "imie",
    #     "nazwisko",
    #     "telefon",
    #     "towar",
    #     "paragon",
    #     "faktura",
    #     "cena_zakupu",
    #     "dane_do_zwrotu",
    #     "powod_zwrotu",
    #     "data_odebrania_towaru",
    # ]


# Register your models here.
admin.site.register(Zwrot, ZwrotAdmin)
