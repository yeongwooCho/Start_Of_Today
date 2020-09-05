from django.shortcuts import render
from django.http import HttpResponse
from .youtube import get_vid
from .models import Video
from .scraping import scraping

# Create your views here.


def motivation(request):
    videos = Video.objects.filter(num='공부 동기부여')
    return render(request, "youtube.html", {'videos': videos})


def career(request):
    videos = Video.objects.filter(num='취업 팁')
    return render(request, "youtube.html", {'videos': videos})


def coding(request):
    videos = Video.objects.filter(num='코딩테스트')
    return render(request, 'youtube.html', {'videos': videos})
