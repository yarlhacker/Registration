from django.db import models
from django.contrib.auth.models import User 


class Base(models.Model):

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta : 
        abstract = True


class Profil(Base):
    user = models.OneToOneField(User, verbose_name=("Userdjango"), on_delete=models.CASCADE)
    prenom = models.CharField(max_length=250, null=True, blank=True)
    photo = models.FileField(upload_to='Images', null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)


    def __str__(self):
        return self.prenom
    
    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profils'


class Contact(Base):

    user = models.ForeignKey(User, verbose_name=("Profil"), on_delete=models.CASCADE)
    photo = models.FileField(upload_to='Images', null=True, blank=True)
    nom = models.CharField( max_length=250)
    prenom = models.CharField( max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField( max_length=250)


    def __str__(self):
        return self.nom
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


# Create your models here.
