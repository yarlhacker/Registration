from django.contrib import admin
from . import models 


@admin.register(models.Profil)
class ProdilAdmin(admin.ModelAdmin):

    list_display = ["user","prenom","photo","phone", "date_creat","date_update","status"]
    list_editable = ('status',)



@admin.register(models.Contact)
class ProdilAdmin(admin.ModelAdmin):

    list_display = ["user","prenom","photo","phone","nom","email", "date_creat","date_update","status"]
    list_editable = ('status',)

    


# Register your models here.
