from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name


class BLOG(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=500)
    banner = models.ImageField(upload_to='blog/banners', blank=True, null=True)
    description = RichTextField()
    author_pic = models.ImageField(
        upload_to='blog/profile_pic', default='banners/avatar.jpg')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class COMMENT(models.Model):
    post = models.ForeignKey(
        BLOG, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    author = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    created = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.author
