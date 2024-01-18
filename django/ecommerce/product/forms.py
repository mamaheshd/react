from django.forms import ModelForm,fields
from .models import *

class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'