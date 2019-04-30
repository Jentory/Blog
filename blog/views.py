from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from . import models

def index(request):
    #return HttpResponse('Hello,World!')
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})



