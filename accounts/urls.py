from django.urls import path
from . import views

# namespace = 같은이름의 파일이 있을때 사용
app_name = 'accounts'
urlpatterns = [
    path('homepage/', views.homepage, name="homepage"), # 홈페이지 urlpatterns
    path('sign-up/', views.sign_up, name="sign_up"), # 회원가입 urlpatterns
]
