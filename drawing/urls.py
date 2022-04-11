from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index2, name='index2'),
    path("drawing/canvas", views.Index, name='index'),
    path("drawing/canvas2", views.Canvas, name='canvas'),
]