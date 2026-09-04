from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='game1'),
    path('rps/', views.rps, name='rps'),
    path('quiz/', views.quiz, name='quiz'),
]