from django.db import models

# Create your models here.
class Blog(models.Model):
    """
    create columns :
    title : to store blog title
    sub title: to store blog sub title
    author : to author name
    blog cotent ,short description, image
    created at field and updated at field 
    """
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255,blank=True,null=True)
    author =models.CharField(max_length=120)
    content = models.TextField()
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True,null=True)
    draft =  models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    
