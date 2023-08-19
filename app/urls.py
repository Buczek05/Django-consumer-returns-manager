from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path("", views.Zwroty_List_View.as_view(), name="list"),
    path("edit/<int:pk>", views.Zwroty_Edit.as_view(), name="edit"),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path("create", views.Zwroty_Create.as_view(), name="create"),
]
