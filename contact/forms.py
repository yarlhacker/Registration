from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from . import models


class ProfilForm(ModelForm):
    class Meta:
        model = models.Profil
        fields = '__all__'
        exclude = ['user']

class CreateProfilForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['username', 'email', 'password1', 'password2']

class ContactForm(ModelForm):
    class Meta:
        model = models.Contact
        fields = '__all__'
        exclude = ['user']