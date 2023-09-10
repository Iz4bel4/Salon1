from django.db import models
from django.contrib import admin
import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class OfferType:
    Treatment = 'Treatment'
    Make_up = 'Make up'
    Manicure = 'Manicure'

    CHOICES = (
        (Treatment, 'Treatment'),
        (Make_up, 'Make up'),
        (Manicure, 'Manicure'),
    )

class Offer(models.Model):
    name = models.CharField(max_length=200 ,null=False, unique=True)
    price = models.FloatField(null=False, default=0)
    type = models.CharField(max_length=20, choices=OfferType.CHOICES, default='')

    def __str__(self):
        return self.name
    
class Aboutus(models.Model):
    description = models.TextField(max_length=600 ,null=False)

    def __str__(self):
        return self.description
    
class WorkPictures(models.Model):
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
       return str(self.image)
    


class Blog(models.Model):
    my_date = models.DateField(default=datetime.date(1111, 1, 1))
    author = models.CharField(max_length=100, default="author's name")
    image = models.ImageField(upload_to='static/images/')
    topic = models.CharField(max_length=200)
    first_sentence = models.CharField(max_length=200, default='')
    content = RichTextField()
    
    def __str__(self):
        return self.topic

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)