from django.urls import path
from . import views


# namespace = 같은이름의 파일이 있을때 사용
app_name = 'products'
urlpatterns = [
    path("", views.products, name="products"),  # 글 목록
    path("<int:pk>/", views.post_detail, name="post_detail"),  # 게시물 디테일
    path("post_upload/", views.post_upload, name="post_upload"),  # 게시글 작성 페이지
    # 게시글 업데이트 페이지('게시글 번호/업데이트')
    path('<int:pk>/update/', views.update, name='update'),
    path("<int:pk>/delete/", views.delete, name='delete'),      # 게시글 삭제 페이지
    path('<int:pk>/like/', views.like, name='like'),            # 게시글 좋아요
    path("search/", views.search, name="search"),               # 검색
]
