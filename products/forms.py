from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = "__all__"   # 아티클에 있는 내용 다 적을 거임
        exclude = ('author', 'like_users', 'n_hit')   # author 빼고 다 포함
