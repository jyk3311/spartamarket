from django.conf import settings
from django.db import models


class Article(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 작가라는 필드(글과 연관, on_delete 속성값은 참조하고 있는 값을 어떻게 할건지 결정, CASCADE 연쇄적으로 삭제)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles'
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_articles'
    )

    # 조회수 테이블
    n_hit = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="post"
    )

    # 찜한 수 계산
    @property
    def like_count(self):
        return self.like_users.count()

    def __str__(self):
        return self.title
