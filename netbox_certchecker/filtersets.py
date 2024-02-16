# filtersets.py
import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from .models import Certificate

class FilterCertificate(NetBoxModelFilterSet):
    class Meta:
        model = Certificate
        fields = ( 'id', 'name', 'url', 'alert', 'created', 'last_updated')
