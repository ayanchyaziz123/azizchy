from django.db import models
from django import forms
from PIL import Image


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    postAuthor = models.CharField(max_length=200)
    postId = models.AutoField(primary_key=True, auto_created=True)
    postTitle = models.CharField(max_length=200)
    postTimeDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    postText = models.TextField()
    postUrl = models.TextField(blank=True)
    postImage = models.ImageField(blank=True, null=True)

    

    def get_photo_url(self):
        if self.postImage and hasattr(self.postImage, 'url'):
            return self.postImage.url
        else:
            return "/static/no.png"

    #image resizing




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'postTitle', 'postText', 'postImage']


class Contact(models.Model):
    siNo = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
    Email = models.CharField(max_length=100)
    TellUs = models.TextField()
    DateTime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From: ' + self.Name + ' Email address : ' +self.Email