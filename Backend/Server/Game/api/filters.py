import django_filters
from employees.models import Social

class SocialFilter(django_filters.FilterSet):
    soc_name = django_filters.CharFilter(field_name='soc_name', lookup_expr='iexact')
    class Meta:
        model = Social
        fields = ['soc_name']