from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200,default='Title not available')
    head0 =models.CharField(max_length=200 , default='Heading 0')
    chead0 =models.CharField(max_length=5000 , default='CHeading 0')
    head1 =models.CharField(max_length=200 , default='Heading 1')
    chead1 =models.CharField(max_length=5000 , default='CHeading 1')
    head2 =models.CharField(max_length=200 , default='Heading 2')
    chead2 =models.CharField(max_length=5000, default='CHeading 2')
    pubdt =models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='blog/images',default='blog/images/Screenshot_2.png')

    def __str__(self):
        return self.title
