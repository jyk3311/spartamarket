from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# @login_required # 로그인을 해야만 화면이 보임.
# def user(request):
#     user = request.user
#     items = user.items.all()  # 유저가 등록한 물품들 불러오기
#     return render(request, 'user.html', {'user': user, 'items': items})

def profile(request, username):
    member = get_object_or_404(get_user_model(), username = username) # db 탐색 후, 회원이 있는지 없는지 확인하는 작업 ##
    context = {
        "member" : member
    }
    return render(request,'user/profile.html', context)