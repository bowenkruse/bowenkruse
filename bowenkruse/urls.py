from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wumpus/', views.wumpus, name='wumpus'),
    path('biocalc/', views.bioCalc, name='biocalc'),
    path('sudoku/', views.sudoku, name='sudoku'),
    path('ticktacktoe/', views.ticktacktoe, name='ticktacktoe'),
    path('onetwoseven/', views.onetwoseven, name='onetwoseven'),
    path('uxwork/', views.uxwork, name='uxwork'),
    path('wesyncux/', views.wesyncUX, name='wesyncUX')
]
