from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name='index'),
    path("drawing/canvas", views.Canvas, name='canvas'),

]