from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from . import models
# Create your forms here.


class Utilisateur(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(Utilisateur, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Veuillez entrer votre nom d'utilisateur : "
        self.fields['email'].label = "Veuillez entrer votre adresse mail : "
        self.fields['password1'].label = "Veuillez entrer votre mot de passe : "
        self.fields['password2'].label = "Veuillez confirmer votre mot de passe : "

    def save(self, commit=True):
        user = super(Utilisateur, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class Authentification(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Nom d'utilisateur : "
        self.fields['password'].label = 'Mot de Passe : '
