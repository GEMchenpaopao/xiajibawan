from django.contrib import admin
from .models import *
# Register your models here.
class AuthorManage(admin.ModelAdmin):
    list_display = ['id','name']
class BookManage(admin.ModelAdmin):
    list_display = ['id','title']
#不能有list_display=['id','title','authors'],因为两者不存在直接关联

admin.site.register(Author,AuthorManage)
admin.site.register(Book,BookManage)

