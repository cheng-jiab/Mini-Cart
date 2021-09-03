from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'firstName',
            'lastName',
            'phone',
            'email',
            'addressLine1',
            'addressLine2',
            'country',
            'state',
            'city',
            'orderNote',
        ]