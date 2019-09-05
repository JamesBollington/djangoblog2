from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

#parent
class Categories(models.Model):
    Category_name=models.CharField(max_length=100)
    slug=models.SlugField()
#child
class Post(models.Model):
    Title=models.CharField(max_length=100)
    Date=models.DateTimeField()
    Body=models.TextField()
    Category=models.ManyToManyField('Categories')
    slug=models.SlugField()


class Comment(models.Model):
    Name=models.CharField(max_length=100)
    Comment=models.TextField()
    Post=models.ForeignKey('Post',on_delete=models.CASCADE)
