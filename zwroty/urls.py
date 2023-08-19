"""zwroty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.urls import re_path as url

admin.site.site_header = "TECHTRONIC"
admin.site.site_title = "TECHTRONIC"
urlpatterns = i18n_patterns(
    # ...
    # path("admin/backups/", include("dbbackup_ui.urls")),
    path("admin", admin.site.urls),
    path("", include("app.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    # path("admin/", admin.site.urls),
    # ...
    # If no prefix is given, use the default language
    prefix_default_language=False,
)
