from django.urls import path
from . import views


# namespace = 같은이름의 파일이 있을때 사용
app_name = 'products'
urlpatterns = [
    path("post_detail/", views.post_detail, name = "post_detail"),  # 게시 물건 디테일 urlpatterns

]
