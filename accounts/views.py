from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm



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


@login_required
@require_http_methods(["GET", "POST"])
def update(request):
    if request.method == "POST":
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

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:homepage')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, "accounts/change_password.html", context)
