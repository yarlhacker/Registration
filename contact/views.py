from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,UserManager
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from .filter import search


# from django.urls import reverse
import json

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
    except:
        return False

def checkup(request):
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
            user = User.objects.create_user(username=email,password=pwd,email=email)
            profil = models.Profil(photo=photo,prenom=prenom,phone=phone , user=user)
            profil.save()

            return redirect("index")
    datas= {
        'success': success,
        'msg': msg,
    }
    return JsonResponse(datas, safe=False)

def inscription(request):
    return render(request,'inscription.html')

def logout_view(request):
    
    logout(request)
    
    return redirect('index')
    

@login_required(login_url='index')
def contact(request):
    find = True
    contacts = models.Contact.objects.filter(status=True, utilisateur=request.user).order_by('nom')
    search_contact = request.GET.get('search_name')
    if search_contact:
        contacts = models.Contact.objects.filter(nom__icontains=search_contact)
        find = False
    return render(request, 'contact.html', locals())




@login_required(login_url='index')
def detail(request, id):
    contact = models.Contact.objects.get(id=id)
    contacts = models.Contact.objects.filter(utilisateur=request.user)
    return render(request, 'detail.html',locals())



@login_required(login_url='index')
def edit(request,id):
    contact = get_object_or_404(models.Contact , id =id)

    if request.method == 'POST':
        contact.photo = request.FILES.get('photo')
        contact.nom = request.POST.get('nom')
        contact.prenom = request.POST.get('prenom')
        contact.email = request.POST.get('email')
        contact.phone = request.POST.get('phone')
        contact.save()
        return redirect('detail', id=contact.id)
    

    return render(request, 'edit.html',locals())



@login_required(login_url='index')
def add(request):

    if request.method == 'POST':
        photo = request.FILES.get('photo')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = models.Contact(photo=photo, nom=nom, prenom=prenom, email=email, phone=phone, utilisateur=request.user)
        contact.save()
        return redirect('index')
        

    return render(request, 'add.html',locals())

@csrf_exempt
def delete_contact(request,id):
    messages ,  success = 'supprimer' , True
    contact = get_object_or_404(models.Contact , id =id )
    contact.delete()

    datas = {

        'message' : messages,
        'success' : success
    }
    return JsonResponse(datas, safe=False)
    

def get_my_contact(request):

    datas = {
        'contact': [
            {
                'id': ct.id,
                'nom': ct.nom,
                'phone': ct.phone,
                'url': reverse('detail', kwargs={'id': ct.id}),
                'url2': reverse('delete_contact', kwargs={'id': ct.id}),
                'photo': ct.photo.url if ct.photo else ''
            } for ct in request.user.user_profile.all()

        ]
    }
    return JsonResponse(datas, safe=False)


def search_contact(request):
    contacts = models.Contact.objects.filter(status=True, utilisateur=request.user).order_by('nom')
    if request.method == "GET":
        search_contact = request.GET.get('search_name')
        contacts = models.Contact.objects.filter(nom=search_contact)
    return render(request , "contact.html",locals())


def copy_contact(id_contact, users):
    contact = models.Contact.objects.get(id=id_contact)
    for us in users:
        contact.id = None
        contact.utilisateur = us.user
        contact.save()


@csrf_exempt
def send_contact(request):
    success, message = False, "Echec d'envoie"
    _emails = request.POST.get('tel_list')
    contact = request.POST.get('id')
    emails = json.loads(_emails)

    users = []
    for u in emails:
        user = models.Profil.objects.filter(user__email=u).first()
        if user:
            users.append(user)
    copy_contact(contact, users)

    if len(users) < 1:
        message = 'Aucun utilisateur trouve'
    else:
        message, success = 'Envoie effectue', True

    datas = {
        "success": success,
        "message": message
    }
    return JsonResponse(datas, safe=False)


