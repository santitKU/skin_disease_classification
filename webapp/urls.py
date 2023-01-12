from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('predictImage', views.predictImage, name='predictImage'),
    path('test_label', views.testlabel, name='testlabel'),
]