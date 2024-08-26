from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("<int:user_id>/follow/", views.follow, name="follow"), # 팔로우 기능
    path('<str:username>/', views.profile, name="profile"), # 유저 프로필 페이지
]