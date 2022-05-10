from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView, UpdateView
from allauth.account.views import PasswordChangeView
from django.urls import reverse
from drawing.forms import ProfileForm
from drawing.models import User

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

class ProfileView(TemplateView):
    template_name = 'drawing/profile.html'

class ProfileSetView(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "drawing/profile_set_form.html"

    def get_object(self, queryset=None):
        return self.request.user
    def get_success_url(self):
        return reverse("index")

class ProfileUpdateView(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "drawing/profile_update_form.html"

    def get_object(self, queryset=None):
        return self.request.user
    def get_success_url(self):
        return reverse("profile")
