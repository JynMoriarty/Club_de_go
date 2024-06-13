from .views import Homepage,Inscription,Connexion
from django.urls import path

urlpatterns = [
    path('',Homepage,name='accueil'),
    path('inscription/',Inscription,name='inscription'),
    path('connexion/',Connexion,name='accueil')


]
