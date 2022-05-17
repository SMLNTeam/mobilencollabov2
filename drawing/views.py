from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,ListView,DetailView,UpdateView,DeleteView,RedirectView,TemplateView
)
from allauth.account.views import PasswordChangeView
from django.urls import reverse
from drawing.forms import ProfileForm
from drawing.models import User
from django.contrib import auth
from .models import Post
from .forms import PostForm
from braces.views import LoginRequiredMixin

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


#logout
def logout(request):
    auth.logout(request)
    return redirect('index')


#post
class IndexRedirectView(RedirectView):
    pattern_name='post-list'
    template_name = "posts/post_list.html"
 
class PostListView(LoginRequiredMixin, ListView):
    model=Post
    ordering=['-dt_created'] #정렬 최신순(-안붙일 경우 오래된 순)
    paginate_by=6
    template_name = "posts/post_list.html"

class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post
    template_name = "posts/post_detail.html"

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    form_class=PostForm 
    template_name = "posts/post_form.html"

    def get_success_url(self):
        return reverse('post-detail',kwargs={'pk':self.object.id})



class PostUpdateView(LoginRequiredMixin,UpdateView):
    model=Post
    form_class=PostForm
    template_name = "posts/post_form.html"
    def get_success_url(self) :
        return reverse('post-detail',kwargs={'pk':self.object.id})

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    template_name = "posts/post_confirm_delete.html"

    def get_success_url(self):
        return reverse('post-list')

def Canvas(request):
    return render(request,'posts/canvas.html')
