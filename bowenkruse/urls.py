from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('wumpus/', views.wumpus, name='wumpus'),
    path('biocalc/', views.bioCalc, name='biocalc'),
    path('sudoku/', views.sudoku, name='sudoku'),
    path('ticktacktoe/', views.ticktacktoe, name='ticktacktoe'),
    path('onetwoseven/', views.onetwoseven, name='onetwoseven'),
    path('uxwork/', views.uxwork, name='uxwork'),
    path('wesyncux/', views.wesyncUX, name='wesyncUX'),
    path('underconstruction', views.underconstruction, name='underconstruction')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
