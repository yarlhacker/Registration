from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    return render(request, 'index.html')



def inscription(request):

    if request.method == 'POST' :
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        photo= request.FILES.get('photo')
        pwd = request.POST.get('password')
        confirmpwd = request.POST.get('Confirmpassword')

        contact = models.Profil.objects.create_user(usermane = username, email=email, photo=photo ,last_name=prenom ,password = pwd ,)
        contact.save()

    return render(request, 'inscription.html')




def contact(request):
    return render(request, 'contact.html')





def detail(request):
    return render(request, 'detail.html')





def edit(request):
    return render(request, 'edit.html')




def add(request):
    return render(request, 'add.html')

