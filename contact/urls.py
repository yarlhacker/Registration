from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('inscription/', views.inscription, name='inscription'),
    path('contact/', views.contact, name='contact'),
    path('detail/', views.detail, name='detail'),
    path('edit/', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('getmycontact', views.get_my_contact, name='getmycontact')
]
