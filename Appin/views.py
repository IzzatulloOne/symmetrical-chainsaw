from django.shortcuts import render
from . import models
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def index(request):
    hobby = models.Hobby.objects.all()
    context = {
        'myhobby':hobby,
    }
    return render(request, 'index.html', context)

def generic(request):
    aboutme = models.About_Me.objects.all()
    context = {
        'about':aboutme
    }
    return render(request, 'generic.html',context)

def elements(request):
    blogadventure = models.Blog_adventure.objects.all()
    context = {
        'blog':blogadventure
    }
    return render(request, 'elements.html', context)


