from django import forms
from .models import User

from .models import Post
from django.core.exceptions import  ValidationError

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            "profile_pic",
            "intro",
        }
        Widgets = {
            "intro": forms.Textarea,
        }


class PostForm(forms.ModelForm):
    
    class Meta: 
        model=Post
        fields=['title','content','image']
        widgets={
            'title':forms.TextInput(attrs={
                'class':'title',
                'placeholder':'제목을 입력하세요'
            }),
            'content':forms.Textarea(attrs={    
                'placeholder':'내용을 입력하세요'
            })
        }
    def clean_title(self):
        title=self.cleaned_data['title']
        
        return title
