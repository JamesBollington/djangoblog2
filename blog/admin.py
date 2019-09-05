from django.contrib import admin
from .models import Categories, Post, Comment

# Register your models here.

admin.site.register(Categories)
admin.site.register(Post)
admin.site.register(Comment)
