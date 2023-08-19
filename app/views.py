from django.shortcuts import render
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from app import models, forms
from django.db.models import Q, F
from django.core.paginator import Paginator
from django.urls.base import reverse_lazy
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()


def search_query(self):
    query = self.request.GET.get("q")
    page_obj = models.Zwrot.objects.filter(
        Q(imie__icontains=query)
        | Q(nazwisko__icontains=query)
        | Q(telefon__icontains=query)
        | Q(towar__icontains=query)
    )
    return page_obj, query


def pagin(model, request):
    paginator = Paginator(model, 50)
    page_number = request.GET.get("page")

    return paginator.get_page(page_number)


class Zwroty_List_View(LoginRequiredMixin, ListView):
    model = models.Zwrot
    template_name = "app/zwrot_list.html"

    def get(self, request, *args, **kwargs):
        context = {}
        model = models.Zwrot.objects.order_by("-pk")
        context["zwroty_list"] = pagin(model, request)
        return render(request, self.template_name, context)


class Zwroty_Edit(LoginRequiredMixin, UpdateView):
    context_object_name = "zwrot"
    fields = (
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
        "data_zwrotu_pieniedzy",
    )
    model = models.Zwrot
    success_url = reverse_lazy("list")


class Zwroty_Create(LoginRequiredMixin, CreateView):
    context_object_name = "zwrot"
    fields = (
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
        "data_zwrotu_pieniedzy",
    )
    widget = {
        "imie": forms.TextInput(
            attrs={
                "class": "form-control bg-black text-white",
                "style": "max-width: 300px;",
                "placeholder": "imie",
            }
        ),
        "nazwisko": forms.TextInput(
            attrs={
                "class": "form-control bg-black text-white",
                "style": "max-width: 300px;",
                "placeholder": "nazwisko",
            }
        ),
    }

    model = models.Zwrot
    success_url = reverse_lazy("list")
    REDIRECT_FIELD_NAME = "app/zwrot_form.html"

    def get_success_url(self):
        return reverse("list")


class SearchResultsView(LoginRequiredMixin, ListView):
    model = models.Zwrot
    context_object_name = "zwroty_list"
    template_name = "app/zwrot_list.html"

    def get(self, request, *args, **kwargs):
        context = {}
        model, tit = search_query(self)
        context["zwroty_list"] = model.order_by("-pk")[:100]
        return render(request, self.template_name, context)
