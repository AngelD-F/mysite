import django_filters
from django_filters import DateFilter

from .models import order

class orderFilter(django_filters.FilterSet):
    start_date = DateFilter(
        field_name='date_created',
        lookup_expr='gte',
        label='Creado desde',
    )
    end_date = DateFilter(
        field_name='date_created',
        lookup_expr='lte',
        label='Creado hasta',
    )

    class Meta:
        model = order
        fields = '__all__'
        exclude = ['customer', 'date_created']

