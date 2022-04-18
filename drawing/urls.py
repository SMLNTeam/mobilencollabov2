from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.IndexView.as_view(), name='index'),
    path("editor", views.EditorView.as_view(), name='editor'),
    path("", views.index, name='index'),
    path("", views.editor, name='editor'),
]