from netbox.filtersets import NetBoxModelFilterSet
from .models import StaticRoute, Community

class StaticRouteFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = StaticRoute
        fields = ('id', 'device', 'prefix', 'ip_address')

    def search(self, queryset, name, value):
        return queryset.filter(comments__icontains=value)

class CommunityFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Community
        fields = ('id', 'community', 'description')

    def search(self, queryset, name, value):
        return queryset.filter(comments__icontains=value)
