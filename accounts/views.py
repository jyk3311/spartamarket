from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django import forms
from django.contrib.auth import authenticate, get_user_model, password_validation
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX, identify_hasher


# Create your views here.
def homepage(request):
    return render(request, "accounts/homepage.html")

@require_http_methods(['GET', 'POST'])  # GET, POST 만 받을수 있게 설정
def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:homepage")
    else:
        form = CustomUserCreationForm()

    context = {                    # 양식을 html에 보낸다.
        "form": form
    }
    return render(request, "accounts/sign_up.html", context)

@require_http_methods(['GET', 'POST'])  # GET, POST 만 받을수 있게 설정
def login(request):  # 로그인
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())  # 로그인하는 코드
            next_url = request.GET.get(
                'next') or 'accounts:homepage'  # 로그인 후 어디로 보낼지
            return redirect(next_url)  # 어디로 갈지 설정해
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "accounts/login.html", context)

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('accounts:homepage')
