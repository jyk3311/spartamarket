from django.shortcuts import get_object_or_404, redirect, render
from .models import Article
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.db.models import Q


@login_required
def products(request):

    # GET 요청으로 sort 매개변수값 가져옴/ 기본값은 '-created_at'
    sort_option = request.GET.get('sort', '-created_at')
    print(sort_option)
    products = Article.objects.all().order_by(
        sort_option, '-created_at')  # 사용자의 선택에 따라 정렬
    context = {
        "products": products,

    }
    return render(request, "products/products.html", context)


@login_required
def search(request):
    message = request.GET.get('message')
    print(message)
    products = Article.objects.filter(
        Q(title__icontains=message) | Q(content__icontains=message) | Q(author__username__icontains=message)).distinct()
    context = {
        "products": products,
    }
    return render(request, "products/products.html", context)


@login_required
@require_http_methods(["GET", "POST"])  # get과 post 방식으로만 받겠다.
def post_upload(request):              # 게시물 업로드 함수

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():  # 폼에 있는 데이터들이 유효하다면: 데이터 바인딩(DB 형식이랑 맞다면)
            # 데이터를 저장하고
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('products:products')

    else:

        form = ArticleForm()
    context = {
        "form": form,
    }

    return render(request, "products/post_upload.html", context)


@login_required
def post_detail(request, pk):
    product = get_object_or_404(Article, pk=pk)
    if product.n_hit.filter(pk=request.user.pk).exists():
        pass
    else:
        product.n_hit.add(request.user)
    context = {
        "product": product,
    }
    return render(request, "products/post_detail.html", context)


@login_required
def update(request, pk):
    product = get_object_or_404(Article, pk=pk)    # 번호를 받아서 해당 글을 product 에 저장
    if request.method == 'POST':
        # instance가 비어있으면 새로운것 생성, 아니면 기존 데이터 수정
        form = ArticleForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products:post_detail", product.pk)
    else:
        # instance가 비어있으면 빈것 보여줌. 아니면 받은 인자값 채워서 보여줌
        form = ArticleForm(instance=product)
        context = {
            'form': form,
            'product': product, }
        return render(request, 'products/update.html', context)


@login_required
def delete(request, pk):
    # 일단 내용 받아오고
    product = get_object_or_404(Article, pk=pk)
    # 로그인 되어 있고, 글 작성자와 로그인 유저가 같다면 삭제
    if request.user.is_authenticated and product.author == request.user:
        product.delete()
        return redirect("products:products")


@login_required
@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Article, pk=pk)
        # 지금 로그인한 유저가 이 글을 좋아요 했던게 테이블에 있다면
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)  # 좋아요 취소
        else:
            product.like_users.add(request.user)  # 테이블에 없으니까 좋아요 생성
        return redirect('products:post_detail', product.pk)
    return redirect('accounts:login')


def count(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Article, pk=pk)

        return
