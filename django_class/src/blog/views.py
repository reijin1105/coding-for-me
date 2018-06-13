# 알파벳 순서대로 정렬
#from django.http import HttpResponse
from django.shortcuts import render
#from random import randint
# models에 있는 걸 이용하려면 여기서 임포트해줘야함 -> 그러고나야 html에 표시
from .models import Article

# 서버를 돌릴 때마다 실행시키는 곳이 바로 blog의 view (디자인적으로 보여주는 곳은 html 파일)
def index(request):
    #random_number=randint(1,10)
    #return HttpResponse("Hello, world. {}".format(random_number))
    #return HttpResponse("Hello, world. You're at the index.")
    #name="taeho"
    #return render(request,"index.html",{"name":name})
    article_list=Article.objects.all()
    #Article.objects.create(
        #title="hello",
        #contents="this is test", # 리스트 안에 콤마 찍는거 잊지말자.
        #view_count=0
    #)
    ctx={
        "article_list":article_list
    }
    return render(request,"index.html",ctx)
