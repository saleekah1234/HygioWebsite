from django import forms
from .models import Order


class OrderForm(forms.ModelForm):


    class Meta:
        model = Order
        fields = ('name','item')
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['name'].widget.attrs['rows'] = 5
        self.fields['item'].widget.attrs['rows'] = 5