from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    view_count= models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.title,self.view_count)

class Comment(models.Model):
    article = models.ForeignKey(Article)
    comment = models.CharField(max_length=300)
