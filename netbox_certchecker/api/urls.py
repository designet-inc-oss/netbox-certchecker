from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_certchecker'

router = NetBoxRouter()
router.register('certchecker', views.CertificateViewSet)

urlpatterns = router.urls
