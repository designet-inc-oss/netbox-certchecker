import django_tables2 as tables
from django.utils.translation import gettext as _
from django.utils.html import format_html
from netbox.tables import NetBoxTable, ChoiceFieldColumn, columns
from .models import Certificate

class CertificateTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    device = columns.ManyToManyColumn(
        verbose_name=_('Device'),
        linkify_item=('dcim:device', {'pk': tables.A('pk')})
    )

    class Meta(NetBoxTable.Meta):
        model = Certificate
        fields = ('pk', 'id', 'name', 'cert', 'url', 'alert','comments', 'device', 'actions', )
        default_columns = ('name', 'url' 'cert', 'alert')


