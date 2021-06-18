from . import models 
import django_filters


class search(django_filters.FilterSet):
    nom = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = models.Contact
        fields = ['nom']