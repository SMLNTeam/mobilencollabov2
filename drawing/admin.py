from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Post

# Register your models here.
admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (("user fields", {"fields": ("profile_pic", "intro")}), )
admin.site.register(Post)