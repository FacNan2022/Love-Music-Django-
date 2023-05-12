from django.http import HttpResponse
from django.shortcuts import render

def karaoke(request):
    return render(request, 'karaoke.html', {}) 

def inicio(request):
    return render(request, 'inicio.html', {})

def reproductor(request):
    return render(request,'reproductor.html', {})

def video(request):
    return render(request, 'video.html', {})

 
