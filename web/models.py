from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    title = models.CharField(max_length=100)

class Blog(models.Model):
    heading = models.CharField(max_length=300)
    date = models.DateField(auto_now= True)
    mini_content = models.TextField()
    image = models.ImageField(upload_to='blog')
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)


