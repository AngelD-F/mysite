import django_filters

from .models import order

class orderFilter(django_filters.FilterSet):
    class Meta:
        model = order
        fields = '__all__'

