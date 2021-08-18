from django import forms
from django.forms.widgets import TextInput


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

# class NumberInput(TextInput):
#     input_type = 'number'
#
# homework = forms.FloatField(required=False, max_value=10, min_value=1,
#                             widget=NumberInput(attrs={'id': 'form_homework', 'step': "1"}))

