from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer
from ..models import Certificate

class CertificateSerializer(NetBoxModelSerializer):

    class Meta:
        model = Certificate
        fields = ( 'id', 'name', 'url', 'cert','device', 'alert', 'comments', 'tags', 'custom_fields', 'created', 'last_updated')

