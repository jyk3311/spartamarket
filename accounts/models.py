from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Accounts(models.Model):
    image = models.ImageField(upload_to="images/", blank=True)

class User(AbstractUser):
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers"
    )
