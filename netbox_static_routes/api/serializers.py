from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer, WritableNestedSerializer
from ..models import StaticRoute, Community
from ipam.models import IPAddress, Prefix
from dcim.models import Device

class NestedDeviceSerializer(WritableNestedSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'display']

class NestedPrefixSerializer(WritableNestedSerializer):
    class Meta:
        model = Prefix
        fields = ['id', 'prefix', 'display']

class NestedIPAddressSerializer(WritableNestedSerializer):
    class Meta:
        model = IPAddress
        fields = ['id', 'address', 'display']

class NestedCommunitySerializer(WritableNestedSerializer):
    class Meta:
        model = Community
        fields = ['id', 'community', 'display']

class StaticRouteSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_static_routes-api:staticroute-detail'
    )

    device = NestedDeviceSerializer()

    prefix = NestedPrefixSerializer()

    ip_address = NestedIPAddressSerializer()

    discard = serializers.BooleanField()
    
    communities = NestedCommunitySerializer(many=True)

    class Meta:
        model = StaticRoute
        fields = (
            'id', 'url', 'display', 'device', 'prefix', 'ip_address', 'discard', 'communities', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated',
        )

class CommunitySerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_static_routes-api:community-detail'
    )

    class Meta:
        model = Community
        fields = (
            'id', 'url', 'display', 'community', 'description', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated',
        )