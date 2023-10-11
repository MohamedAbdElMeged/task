from django.urls import path, include

from . import views

urlpatterns = [
    path('validate', views.validate, name='validate'),



]
