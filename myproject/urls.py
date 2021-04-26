"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView

from teagasc import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("importExport", views.importExport, name="importExport"),
    path("importExportReport", views.importExportReport, name="importExportReport"),
    path(
        "conductGrasslandAssessment",
        views.conductGrasslandAssessment,
        name="conductGrasslandAssessment",
    ),
    path(
        "conductGrasslandAssessment2",
        views.conductGrasslandAssessment2,
        name="conductGrasslandAssessment2",
    ),
    path(
        "conductGrasslandAssessment3",
        views.conductGrasslandAssessment3,
        name="conductGrasslandAssessment3",
    ),
    path(
        "conductGrasslandAssessment4",
        views.conductGrasslandAssessment4,
        name="conductGrasslandAssessment4",
    ),
    path(
        "conductGrasslandAssessment5",
        views.conductGrasslandAssessment5,
        name="conductGrasslandAssessment5",
    ),
    path(
        "grasslandReport",
        views.grasslandAssessmentResult,
        name="grasslandAssessmentResult",
    ),
    path("storage", views.storage_process, name="storage"),
    path("updateLsu", views.update_lsu, name="updateLsu"),
    path("records", views.view_records, name="records"),
    path("storage_report", views.storage_report, name="storage_report"),
    path("accounts/", include("django.contrib.auth.urls")),
]
