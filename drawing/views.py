from django.shortcuts import render
from django.views.generic import TemplateView
from allauth.account.views import PasswordChangeView
from django.urls import reverse

# Create your views here.
class IndexView(TemplateView):
    template_name = 'drawing/index.html'
class EditorView(TemplateView):
    template_name = 'drawing/editor.html'
def index(request):
    return render(request, 'drawing/index.html')

def editor(request):
    return render(request, 'drawing/editor.html')

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")