from netbox.api.viewsets import NetBoxModelViewSet

from .. import models, filtersets
from .serializers import CertificateSerializer

class CertificateViewSet(NetBoxModelViewSet):
    queryset = models.Certificate.objects.prefetch_related('tags')
    serializer_class = CertificateSerializer
    filterset_class = filtersets.FilterCertificate
