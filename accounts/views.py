from django.shortcuts import render
from django.views.decorators.http import require_POST, require_http_methods


# Create your views here.
def homepage(request):
    return render(request, "accounts/homepage.html")


@require_http_methods(['GET', 'POST']) # GET, POST 만 받을수 있게 설정
def sign_up(request):
    # if request.method == 'POST':
    # form = CustomUserCreationForm(request.POST)
    return render(request, "accounts/sign_up.html")
