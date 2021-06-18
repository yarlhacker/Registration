from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Profil)
class ProfilAdmin(admin.ModelAdmin):
    
    list_display = ["user","prenom","images_view","phone","status"]
    list_editable = ('status',)

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="height:100px; width:200px">')

    images_view.short_description = 'Aperçu des images'

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ["utilisateur","prenom","images_view","phone","nom","email", "date_add","date_update","status"]
    list_editable = ('status',)

    def images_view(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="height:100px; width:200px">')

    images_view.short_description = 'Aperçu des images'
    


# Register your models here.
