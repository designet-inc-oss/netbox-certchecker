from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse

class Certificate(NetBoxModel):
    name = models.CharField(
        max_length=254,
        help_text='Certificate name.'
    )
    url = models.URLField(
        max_length=1024,
        help_text='Certificate and associated URL. Use the check tool to periodically access HTTPS and check the expiration date of the certificate.'
    )
    comments = models.TextField(
        blank=True
    )
    device = models.ManyToManyField(
        to='dcim.Device',
        blank=True,
        verbose_name='Device',
        help_text='Device with certificate installed'
    )

    cert = models.FileField(
        upload_to='certchecker/%Y/%m/%d/',
        verbose_name='Certificate_file',
        help_text='You can upload your certificate file. This file is not used for monitoring.'
    )

    alert = models.BooleanField(
        default=True,
        help_text='Controls enable/disable of alerts. It can also be used to temporarily stop alerts.'
    )

    def get_absolute_url(self):
        return reverse('plugins:netbox_certchecker:certificate', args=[self.pk])

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):

        super().delete(*args, **kwargs)

        # Delete file from disk
        self.cert.delete(save=False)

