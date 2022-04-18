from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters


# Create your models here.
class User(AbstractUser):
    pass