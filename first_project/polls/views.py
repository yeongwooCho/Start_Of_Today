from django.shortcuts import render
from django.http import HttpResponse
from .youtube import get_vid

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def motivation(request):
    videos = get_vid("공부 동기부여")
    return render(request, "youtube.html", {'videos': videos})


def career(request):
    videos = get_vid("취업 팁")
    return render(request, "youtube.html", {'videos': videos})


def coding(request):
    videos = get_vid("코딩테스트")
    return render(request, 'youtube.html', {'videos': videos})
