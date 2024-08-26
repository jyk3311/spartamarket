from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm


def homepage(request):
    return render(request, "accounts/homepage.html")

# GET, POST 만 받을수 있게 설정


@require_http_methods(['GET', 'POST'])
def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:homepage")
    else:
        form = CustomUserCreationForm()

    # 양식을 html에 보낸다.
    context = {
        "form": form
    }
    return render(request, "accounts/sign_up.html", context)


@require_http_methods(['GET', 'POST'])
def login(request):  # 로그인
    if request.method == "POST":
        # 로그인 폼 (인자값은 유저가 입력한 값이 들어있음)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())  # 로그인하는 함수
            next_url = request.GET.get(
                'next') or 'accounts:homepage'  # 로그인 후 어디로 보낼지
            return redirect(next_url)  # 어디로 갈지 설정해줌
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    # 로그인 했는지 묻는 코드
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('accounts:homepage')


@login_required  # 로그인이 안되어있으면 로그인 요청
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
        # 파일 입력시 인자값으로 request.FILES넘겨줘야함.
        form = CustomUserChangeForm(
            request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("accounts:homepage")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


@login_required
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('accounts:homepage')


@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # 비밀번호 변경 함수
            return redirect('accounts:homepage')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, "accounts/change_password.html", context)
