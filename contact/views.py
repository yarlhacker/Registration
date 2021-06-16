from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,UserManager
from django.contrib.auth import authenticate,login,logout
# from django.urls import reverse
from . import forms
from . import models
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('contact')

    if request.method == 'POST':
        username = request.POST.get('nom')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('contact')
        else:
            print("error")
        # Return an 'invalid login' error message.
    return render(request, 'index.html', locals())

def is_email(email):
    try:
        validate_email(email)
        return True
    except :
        return False


def inscription(request):
    msg , success = '' , False
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pwd = request.POST.get('password1')
        pwd1 = request.POST.get('password2')

        if not photo :
            msg = 'veuillez ajouter une photo'
        elif not nom or nom.isspace():
            msg = 'veuillez remplir ce champs'
        elif not prenom or prenom.isspace():
            msg = 'veuillez remplir ce champs'
        elif not phone or phone.isspace():
            msg = 'veuillez rentrez un numero'
        elif not pwd or pwd.isspace():
            msg = 'veuillez rentrez un mot de passe'
        elif pwd != pwd1 :
            msg = 'veuillez entrer different'
        elif is_email(email):
            msg = 'veuillez rentrez un email valide'
        else:
            success = True

            user = User.objects.create_user(username=nom,password=pwd,email=email)
            user.save()
            profil = models.Profil(photo=photo,prenom=prenom,phone=phone)
            profil.user = user
            profil.save()

            return redirect("index")

    return render(request, 'inscription.html', locals())

def logout_view(request):
    
    logout(request)
    
    return redirect('index')

   


def contact(request):
    
    contacts = models.Contact.objects.filter(status=True, user=request.user).order_by('nom')
    return render(request, 'contact.html', locals())





def detail(request):
    
    return render(request, 'detail.html')





def edit(request):
    return render(request, 'edit.html')




def add(request):
    return render(request, 'add.html')




# def get_my_contact(request):
#     datas = {
#         'contact': [
#             {
#                 'id': ct.id,
#                 'nom': ct.nom,
#                 'telephone': ct.phone,
#                 'url': reverse('detail', kwargs={'id': ct.id}),
#                 'photo': ct.photo.url if ct.photo else ''
#             } for ct in request.user.user_profile.all()

#         ]
#     }

#     return JsonResponse(datas, safe=False)