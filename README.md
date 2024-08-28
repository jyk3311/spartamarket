# spartamarket
Project 이름 : spartamarket
프로젝트 기간 : 2024.08.19 ~ 08.28
개발언어 : Python & Django
팀 멤버 : 김경민,김진영,차민승,남지민
기능 : 회원가입, 로그인, 로그아웃, 게시글 작성, 게시글 수정, 게시글 목록, 게시글 삭제, 
좋아요, 팔로우기능, 인기/최신순 정렬기능, 검색, 프로필 수정, 회원 정보 변경


프로젝트 소개
spartamarket은 sparta 수강캠프 AI_7기 인원들이 사용할 수 있는 우리만의 중고거래 사이트 입니다.



$단, 구매 및 거래는 불가능 합니다$

---------------------------------------------------------------------------------------------------------------------

1. app별 소개
I . accounts app
- 기능
[1] forms.py 
 1) 회원가입
 2) 회원 정보 변경

[2] models.py
class User - AbstractUser 상속
자세한 내용은 공식문서를 https://docs.djangoproject.com/en/5.1/topics/auth/customizing/ 참조

 - following : manytomanyfield 활용
 - profile_image : imagefield 활용

II. products app
- 기능
[1] forms.py
 1) articleForm(form.modelform):

[2] models.py
class Article - models.model 상속
자세한 내용은 공식문서를 https://docs.djangoproject.com/en/5.1/topics/db/models/ 참조
 - image
 - title
 - price
 - created_at
 - updated_at
 - author
 - like_users
 - n_hit
 - like_count

---------------------------------------------------------------------------------------------------------------------

2. 필수 라이브러리
Asgiref == 3.8.1
Django == 4.2
Pillow == 10.4.0
Sqlparse == 0.5.1
typing_extensions == 4.12.2
Tzdata == 2024.1

---------------------------------------------------------------------------------------------------------------------

3. 버그 및 디버그
- . bug: 로그인 안해도 url주소를 치면 글 목록 등 권한 없이 넘어갈수 있는 이슈
-> 권한 필요한 함수에 login데코레이터 삽입.

bug: 조회수가 새로고침이나 찜, 팔로잉 버튼을 누를때마다 증가
-> MTM 방식으로 구현

---------------------------------------------------------------------------------------------------------------------

4. 참고 및 출처
- Bootstrap https://getbootstrap.kr/
- Font https://fonts.google.com/specimen/Hahmlet?subset=korean&script=Kore