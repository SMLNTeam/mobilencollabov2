from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class IndexView(TemplateView):
    template_name = 'drawing/index.html'

class EditorView(TemplateView):
    template_name = 'drawing/editor.html'
