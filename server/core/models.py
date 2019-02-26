from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('email address', unique=True) # changes email to unique and blank to false

    REQUIRED_FIELDS = [] # removes email from REQUIRED_FIELDS
    USERNAME_FIELD = 'email'