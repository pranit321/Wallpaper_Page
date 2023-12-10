from django.shortcuts import render

# Create your views here.

def wallpaper(request):
    return render(request,'wallpaper.html')