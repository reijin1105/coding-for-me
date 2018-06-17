from django.contrib import admin
from .models import Article, Comment

@admin.register(Article, Comment)
class HomeworkAdmin(admin.ModelAdmin):
    pass
