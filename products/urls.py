from django.urls import path
from . import views


# namespace = 같은이름의 파일이 있을때 사용
app_name = 'products'
urlpatterns = [
    path("", views.products, name= "products"),
    path("<int:pk>/", views.post_detail, name = "post_detail"),  # 게시 물건 디테일 urlpatterns
    path("post_upload/", views.post_upload, name = "post_upload"),  # 물건 게시글 작성 페이지 urlpatterns
    path('<int:pk>/update/', views.update, name='update'),         # 게시글 번호/업데이트
    path("<int:pk>/delete/", views.delete, name='delete'),
    path('<int:pk>/like/', views.like, name='like'),
    path("search/", views.search, name="search"),
]
