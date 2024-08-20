from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm): # 회원가입 class
    class Meta: # __init__ 개념이 조금은 비슷하다.
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ()  #() 안에 추가로 넣을 것들 ex) 팔로우 등등등 