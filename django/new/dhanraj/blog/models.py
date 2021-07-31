from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)    
    title = models.CharField(max_length=300) 
    subtitle = models.CharField(max_length=500,default=" ")
    content = models.TextField(default=" ")
    timestamp = models.ImageField(default='default.jpg',height_field=None, width_field=None, upload_to='static')

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})      


    

