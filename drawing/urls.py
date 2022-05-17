from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index", views.IndexView.as_view(), name='index'),

    path("editor", views.EditorView.as_view(), name='editor'),
    path("", views.index, name='index'),
    path("", views.editor, name='editor'),
    path("profile", views.ProfileView.as_view(), name='profile'),
    path("set-profile/", views.ProfileSetView.as_view(), name="profile-set"), 
    path("edit-profile/",views.ProfileUpdateView.as_view(), name="profile-update"),

    path('logout/', views.logout, name = 'logout'),

    path('posts/',views.PostListView.as_view(),name='post-list'),
    path('posts/new',views.PostCreateView.as_view(),name='post-create'),
    path('posts/<int:pk>',views.PostDetailView.as_view(),name='post-detail'),
    path('posts/<int:pk>/edit',views.PostUpdateView.as_view(),name='post-update'),
    path('posts/<int:pk>/delete',views.PostDeleteView.as_view(),name='post-delete'),
    path('posts/canvas',views.Canvas,name='canvas'),
]