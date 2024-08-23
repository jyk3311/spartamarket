from django.contrib import admin
from .models import Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at") # 보여주고 싶은 메뉴를 추가
    search_fields = ("title", "content") # 검색창 생성 및 검색하는 요소 설정
    list_filter = ("created_at",) # 필터링 드롭박스 기능 제공
    date_hierarchy = "created_at" # 날짜별로 조회 가능
    ordering = ("-created_at",) # 정렬 순서 결정

    # 이외에 타이틀은 변경못하게 읽기만 가능하게 하는 read_only 같은 것들을 커스터마이징 해서 쓸 수 있음.
