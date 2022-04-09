import django_filters
from django_filters import DateFilter

from .widgets import DatePickerInput
from .models import order

class orderFilter(django_filters.FilterSet):
    start_date = DateFilter(
        field_name='date_created',
        lookup_expr='gte',
        label='Creado desde',
        widget=DatePickerInput()
    )
    end_date = DateFilter(
        field_name='date_created',
        lookup_expr='lte',
        label='Creado hasta',
        widget=DatePickerInput()
    )

    class Meta:
        model = order
        fields = '__all__'
        exclude = ['customer', 'date_created']
