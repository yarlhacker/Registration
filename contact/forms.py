from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from . import models


class ProfilForm(ModelForm):
    class Meta:
        model = models.Profil
        fields = ['prenom','photo', 'phone']

class CreateProfilForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']