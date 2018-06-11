# 알파벳 순서대로 정렬
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")
