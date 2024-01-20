from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import Product,Category
from .forms import ProductForm,CategoryForm
from django.contrib import messages


# Create your views here.

def index(request):
    # return HttpResponse('This is from the product app view')
    products=Product.objects.all() # get in all to get single values
    category=Category.objects.all()
    context={
        'products':products,
        'category':category,
    }

    return render(request,'product/index.html',context)

def post_product(request):
    # to insert products
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'poroduct added')
            return redirect('/product/addproduct')
        else:
            messages.add_message(request,messages.ERROR,'please validate')
            return render(request,'/product/addproduct.html',{'forms':form})
    #to show add product forms
    context={
        'forms':ProductForm
    }
    return render(request,'product/addproduct.html',context)

def post_category(request):
    # to insert category
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Category added')
            return redirect('/product/addcategory')
        else:
            messages.add_message(request,messages.ERROR,'please validate')
            return render(request,'/product/addcategory.html',{'forms':form})
    #to show add category forms
    context={
        'forms':CategoryForm
    }
    return render(request,'product/addcategory.html',context)
