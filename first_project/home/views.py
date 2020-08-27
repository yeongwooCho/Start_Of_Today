from django.shortcuts import render
from .weather import today, news
from random import randint
# Create your views here.


def home(request):
    article = news()
    weather = today()

    # 명언 파일 읽어서 보내기
    wise_saying = {}
    with open('static/good.txt', 'r', encoding='utf8') as f:
        index = randint(1, 187)
        string = f.readlines()[index]
        if string.find('-') != -1 or string.find('–') != -1:
            li = string.split('-')
            wise_saying['content'] = li[0]
            # if len(li)
            wise_saying['person'] = li[1]
        else:
            wise_saying['content'] = string

    return render(request, "home.html", {'article': article, 'weather': weather, 'wise_saying': wise_saying})
