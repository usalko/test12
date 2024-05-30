from django.forms import ModelForm, FileField, ClearableFileInput
from test12.models import Order


class OrderForm(ModelForm):

    ataches = FileField(widget=ClearableFileInput(attrs={'allow_multiple_selected': True}), required=False)

    class Meta:
        model = Order
        fields = ['email']