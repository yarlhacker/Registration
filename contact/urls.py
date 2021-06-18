from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('inscription/', views.inscription, name='inscription'),
    path('contact/', views.contact, name='contact'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('delete_contact/<int:id>/', views.delete_contact, name='delete_contact'),
    path('getmycontact', views.get_my_contact, name='getmycontact'),
    path('search-contact', views.search_contact, name='search-contact'),
]
