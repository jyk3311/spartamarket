from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


# Create your views here.
def homepage(request):
    return render(request, "accounts/homepage.html")


@require_http_methods(['GET', 'POST']) # GET, POST 만 받을수 있게 설정
def sign_up(request):
    # if request.method == 'POST':
    # form = CustomUserCreationForm(request.POST)
    return render(request, "accounts/sign_up.html")



@require_http_methods(['GET', 'POST']) # GET, POST 만 받을수 있게 설정
def login(request): # 로그인
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get('next') or 'accounts:homepage'
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    
    context = {"form": form}
    return render(request, "accounts/login.html", context)
