from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class Article(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=50)
    price= models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #작가라는 필드(글과 연관)- 
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles'
        ) # User클래스 , 연쇄적으로 삭제 , 별명
    like_users = models.ManyToManyField(
    settings.AUTH_USER_MODEL, related_name='like_articles'
    )
    def __str__(self):
        return self.title