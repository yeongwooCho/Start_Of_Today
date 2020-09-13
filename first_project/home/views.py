from django.shortcuts import render
from .get_wise import get_Wise

# from resultregistration.scraping import scraping
from board.scraping import scraping as bs
from polls.scraping import scraping as ps
# Create your views here.


def home(request):
    wise_saying = get_Wise()

    return render(request, "home.html", {'wise_saying': wise_saying})


def updates(request):
    bs()
    ps()

    return render(request, "updates.html")
