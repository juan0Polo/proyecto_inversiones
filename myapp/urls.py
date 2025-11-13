from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path("usuarios/", include("usuarios.urls")),
    path("proyectos/", include("proyectos.urls")),
]
