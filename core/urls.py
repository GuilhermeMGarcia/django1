"""Define padroes de URL para core."""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('contato', views.contato),
]
