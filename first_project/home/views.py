from django.shortcuts import render
from .get_wise import get_Wise
# Create your views here.


def home(request):
    wise_saying = get_Wise()

    return render(request, "home.html", {'wise_saying': wise_saying})
