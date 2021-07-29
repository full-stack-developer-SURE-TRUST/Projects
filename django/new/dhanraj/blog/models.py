from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)    
    title = models.CharField(max_length=300) 
    subtitle = models.CharField(max_length=500,default=" ")
    content = models.TextField(default=" ")

    def __str__(self):
        return self.title 


    

