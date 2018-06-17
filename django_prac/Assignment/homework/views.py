from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    #return HttpResponse("Hello, Marco. This ia an assignmaent.")
    #name="THEO"
    #return render (request, "in_block.html",{"name"=name})

    article_list=Article.objects.all()
    ctx={"article_list":article_list}
    return render (request, "in_block.html", ctx)
