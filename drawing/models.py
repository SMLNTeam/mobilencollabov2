from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters


# Create your models here.
class User(AbstractUser):

    profile_pic = models.ImageField(
        default="default_profile_pic.jpg"
        , upload_to = "profile_pics"
    )

    intro = models.CharField(max_length=60, blank=True)