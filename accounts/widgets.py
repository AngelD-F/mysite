from django import forms

class DatePickerInput(forms.DateInput):
    template_name = 'widgets/fengyuanchen_datepicker.html'
    