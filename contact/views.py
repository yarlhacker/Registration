from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')



def inscription(request):
    return render(request, 'inscription.html')




def contact(request):
    return render(request, 'contact.html')





def detail(request):
    return render(request, 'detail.html')





def edit(request):
    return render(request, 'edit.html')




def add(request):
    return render(request, 'add.html')

