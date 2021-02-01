from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('姓名',max_length=20)
    def __str__(self):
        return self.name

class Wife(models.Model):
    name = models.CharField('姓名',max_length=20)
    author = models.OneToOneField(Author,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
