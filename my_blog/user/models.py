from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    web_site = models.URLField(max_length=200, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
