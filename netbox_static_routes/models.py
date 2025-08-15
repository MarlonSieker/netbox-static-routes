from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class StaticRoute(NetBoxModel):

    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name=_('Device'),
    )

    prefix = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name=_('Prefix'),
    )

    ip_address = models.ForeignKey(
        to='ipam.IPAddress',
        on_delete=models.PROTECT,
        related_name='+',
        null=True,
        blank=True,
        verbose_name='Next-Hop',
    )

    discard = models.BooleanField(
        default=False,
        verbose_name='Discard route',
        help_text='Discard the route instead of forwarding to a next-hop.'
    )

    communities = models.ManyToManyField(
        to='Community',
        related_name='static_routes',
        blank=True,
    )

    comments = models.TextField(
        blank=True,
    )

    prerequisite_models = (
        'dcim.Device',
        'ipam.Prefix',
        'ipam.IPAddress',
    )
    
    class Meta:
        ordering = ['device','prefix']
        constraints = [
            models.UniqueConstraint(fields=['device', 'prefix'], name='unique_device_prefix')
        ]

    def __str__(self):
        return str(self.prefix)

    def get_absolute_url(self):
        return reverse('plugins:netbox_static_routes:staticroute', args=[self.pk])

class Community(NetBoxModel):

    community = models.TextField()

    description = models.TextField(
        blank=True
    )

    comments = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ['community',]

    def __str__(self):
        return str(self.community)

    def get_absolute_url(self):
        return reverse('plugins:netbox_static_routes:community', args=[self.pk])
