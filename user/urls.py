from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("<int:user_id>/follow/", views.follow, name="follow"), 
    path('<str:username>/', views.profile, name="profile"),
]