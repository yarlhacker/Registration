from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('inscription/', views.inscription, name='inscription'),
    path('contact/', views.contact, name='contact'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('add/', views.add, name='add'),
    path('logout_view/', views.logout_view, name='logout_view'),
    # path('getmycontact', views.get_my_contact, name='getmycontact'),
]
