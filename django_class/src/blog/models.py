from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=30)
    contents=models.TextField()
    view_count=models.IntegerField()

    def __str__(self): # __ 언더바 두 개를 쓰는건 내장된 함수 쓰는 것
        return "{} ({})".format(self.title, self.view_count)

class Comment(models.Model):
    article=models.ForeignKey(Article)
    comment=models.CharField(max_length=100)
