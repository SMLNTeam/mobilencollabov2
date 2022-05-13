from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters
from django.core.validators import MinLengthValidator


# Create your models here.
class User(AbstractUser):

    profile_pic = models.ImageField(
        default="default_profile_pic.jpg"
        , upload_to = "profile_pics"
    )

    intro = models.CharField(max_length=60, blank=True)


class Post(models.Model):
    title=models.CharField(max_length=50,unique=True,error_messages={'unique':'이미 있는 제목입니다.'})
    content=models.TextField(validators=[MinLengthValidator(10,'10자 이상 적어주세요.')])
    image = models.ImageField(upload_to='item_pics')
    dt_created=models.DateTimeField(verbose_name="Date Created",auto_now_add=True)
    dt_modified=models.DateTimeField(verbose_name="Date Modigfied",auto_now=True)

    def __str__(self):
        return self.title