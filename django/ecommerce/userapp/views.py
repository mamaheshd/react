from django.shortcuts import render
from product.models import Product

# Create your views here.
def index(request):
    products=Product.objects.all().order_by('-id')[:8]
    contex={
        'products':products
    }
    return render(request,'user/index.html',contex)