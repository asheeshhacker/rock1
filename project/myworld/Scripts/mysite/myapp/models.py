from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class game(models.Model):
    name = models.CharField(max_length=24,null=True)
    description = models.TextField(null=True)
    #ima = models.ImageField(null=True)


class postdata(models.Model):
    tittle = models.CharField(max_length=60,unique=True)
    slug = AutoSlugField(populate_from='tittle',unique=True)
    body = models.TextField()
    created = models.DateField(auto_now=False, auto_now_add=False)
    pic = models.ImageField(("images"), upload_to='myapp\static\images', height_field=None, width_field=None, max_length=None)

class contdb(models.Model):
    name = models.CharField( max_length=50,null=True)
    mail= models.EmailField( max_length=254,null=True)
    cmt = models.TextField(null=True)
    