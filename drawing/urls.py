from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("drawing/editor", views.EditorView.as_view(), name='editor'),
]