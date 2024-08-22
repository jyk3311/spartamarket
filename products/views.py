from django.shortcuts import render


def post_detail(request):
	id = "지민"
	town = "스파르타 주민"
	title = " 애플 펜슬 2세대 팝니다!"
	price = "120000"
	detail = "개봉하고 한 번 밖에 사용 안해서 깨끗해요."
	
	
	context = {
		"id": id,
		"town": town,
		"title": title,
		"price": price,
		"detail": detail,

		}
	return render(request, "products/post_detail.html", context)


