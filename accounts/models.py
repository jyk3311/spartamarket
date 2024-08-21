from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Accounts(models.Model):
    image = models.ImageField(upload_to="images/", blank=True)

def __str__(self):
    return self.title