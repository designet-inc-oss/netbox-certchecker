from netbox.forms import NetBoxModelForm
from dcim.models import Device
from django.utils.translation import gettext as _
from utilities.forms.fields import CommentField, DynamicModelMultipleChoiceField
from django.forms import URLField, BooleanField, FileField

from .models import Certificate
from .validator import CertificateValidator

class CertificateForm(NetBoxModelForm):

    cert = FileField(required=False,validators=[CertificateValidator()])
    comments = CommentField()

    device = DynamicModelMultipleChoiceField(
        label=_('Device'),
        required=False,
        queryset=Device.objects.all()
    )

    class Meta:
        model = Certificate
        fields = ('name', 'url', 'cert', 'comments', 'device', 'alert')


