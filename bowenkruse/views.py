from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def wumpus(request):
    return render(request, 'wumpus.html')


def bioCalc(request):
    return render(request, 'biocalc.html')


def sudoku(request):
    return render(request, 'sudoku.html')


def ticktacktoe(request):
    return render(request, 'ticktacktoe.html')


def onetwoseven(request):
    return render(request, 'onetwoseven.html')
