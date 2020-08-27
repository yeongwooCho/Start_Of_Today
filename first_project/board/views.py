from django.shortcuts import render
from .models import Board
from .scraping import scraping


def index(request):
    smarts = Board.objects.filter(num='1')
    notices = Board.objects.filter(num='2')
    emps = Board.objects.filter(num='3')
    pusanits = Board.objects.filter(num='4')

    return render(request, 'index.html', {'scp_notices': notices, 'scp_pusanits': pusanits, 'scp_emps': emps, 'scp_smarts': smarts})
