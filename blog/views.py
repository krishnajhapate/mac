from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.

def index(request):
    blogposts=Blogpost.objects.all()
    return render(request,'blog/index.html',{'blogposts':blogposts})

def blogpost(request,id):

    post=Blogpost.objects.filter(post_id=id).first()
    return render(request,'blog/blogpost.html',{'post':post})