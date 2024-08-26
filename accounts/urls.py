from django.urls import path
from . import views

# namespace = 같은이름의 파일이 있을때 구분하기 위하여 사용
app_name = 'accounts'

urlpatterns = [
    path('homepage/', views.homepage, name="homepage"),  # 홈페이지
    path('sign-up/', views.sign_up, name="sign_up"),  # 회원가입
    path('login/', views.login, name="login"),  # 로그인
    path('logout/', views.logout, name="logout"),  # 로그아웃
    path("update/", views.update, name="update"),  # 업데이트
    path("delete/", views.delete, name="delete"),  # 탈퇴
    path('password/', views.change_password, name='change_password'), # 비밀번호 변경
]

