from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

@login_required
def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    articles = member.articles.all()
    like_articles = member.like_articles.all()
    context = {
        "member": member,
        "articles": articles,
        "like_articles": like_articles,
    }
    return render(request, "user/profile.html", context)


@login_required
@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), id=user_id)
        if request.user != member:
            if request.user in member.followers.all():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("user:profile", member.username)
    return redirect("accounts:login")
