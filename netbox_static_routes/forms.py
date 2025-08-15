from django import forms
from ipam.models import Prefix, IPAddress
from dcim.models import Device
from netbox.forms import NetBoxModelForm
from .models import StaticRoute, Community
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm

class StaticRouteForm(NetBoxModelForm):
    comments = CommentField()

    device = DynamicModelChoiceField(
        queryset=Device.objects.all()
    )
    prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all()
    )
    ip_address = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        label='Next-Hop'
    )
    discard = forms.BooleanField(
        required=False,
        label='Discard route'
    )
    communities = DynamicModelMultipleChoiceField(
        queryset=Community.objects.all(),
        required=False,
        label='Communities'
    )

    class Meta:
        model = StaticRoute
        fields = ('device', 'prefix', 'ip_address', 'discard', 'communities', 'comments', 'tags')

    def clean(self):
        super().clean()

        discard = self.cleaned_data.get('discard')
        ip_address = self.cleaned_data.get('ip_address')

        if discard and ip_address:
            self.add_error('ip_address', 'Cannot set both Next-Hop and Discard route.')
        elif not discard and not ip_address:
            self.add_error('ip_address', 'You must specify a Next-Hop or check "Discard route".')

        if discard:
            self.cleaned_data['ip_address'] = None

class StaticRouteFilterForm(NetBoxModelFilterSetForm):
    model = StaticRoute

    device = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )

    prefix = forms.ModelMultipleChoiceField(
        queryset=Prefix.objects.all(),
        required=False
    )

    ip_address = forms.ModelMultipleChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        label='Next-Hop'
    )

    discard = forms.BooleanField(
        required=False,
        label='Discard route'
    )

    community = forms.ModelMultipleChoiceField(
        queryset=Community.objects.all(),
        required=False,
        label='Communities'
    )

class CommunityForm(NetBoxModelForm):
    community = forms.CharField()
    
    description = forms.CharField(
        required=False,
    )

    comments = CommentField()

    class Meta:
        model = Community
        fields = ('community', 'description', 'comments', 'tags')

class CommunityFilterForm(NetBoxModelFilterSetForm):
    model = Community
