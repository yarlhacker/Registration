from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from . import forms
from . import models
# Create your views here.

def index(request):
    return render(request, 'index.html')



def inscription(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        phone = request.POST.get('phone')
        photo = request.FILES.get('photo')
        prenom = request.POST.get('prenom')
        form = forms.CreateProfilForm(
            username = nom,
            email = email,
            password1 = password1,
            password2 = password2
        )
        if form.is_valid():
            user = form.save()
            models.Profil.objects.create(user=user, prenom=prenom, phone=phone, photo=photo)
        return redirect('index')

    return render(request, 'inscription.html')




def contact(request):
    contacts = models.Contact.objects.filter(status=True).order_by('nom')
    return render(request, 'contact.html')





def detail(request):
    
    return render(request, 'detail.html')





def edit(request):
    return render(request, 'edit.html')




def add(request):
    return render(request, 'add.html')




def get_my_contact(request):
    datas = {
        'contact': [
            {
                'id': ct.id,
                'nom': ct.nom,
                'telephone': ct.phone,
                'url': reverse('contact', kwargs={'id': ct.id}),
                'photo': ct.image.url if ct.image else ''
            } for ct in request.user.user_profile.all()

        ]
    }

    return JsonResponse(datas, safe=False)