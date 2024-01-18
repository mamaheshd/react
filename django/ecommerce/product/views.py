from django.shortcuts import render
# from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


# Create your views here.

def index(request):
    # return HttpResponse('This is from the product app view')
    products=Product.objects.all() # get in all to get single values
    context={
        'products':products
    }

    return render(request,'product/index.html',context)
