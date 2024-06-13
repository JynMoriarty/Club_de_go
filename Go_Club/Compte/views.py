from django.shortcuts import render,redirect
from . import forms
from django.urls import reverse_lazy# Create your views here.
from django.views.generic import CreateView 
from django.contrib import messages
from django.contrib.auth import authenticate, login


def Homepage(request):
    return render(request,'accueil.html')


def Inscription(request):
    form = forms.Utilisateur()
    if request.method == 'POST':
        form = forms.Utilisateur(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été crée avec succès !')
            return redirect('connexion')
            
    return render(request,'inscription.html',{'form' : form})

def Connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
    else :
        form = forms.Authentification
        return render(request,'connexion.html',{'form' : form})