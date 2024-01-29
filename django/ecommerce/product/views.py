from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .models import Product,Category
from .forms import ProductForm,CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from userapp.auth import admin_only


# Create your views here.
@login_required
@admin_only
def index(request):
    # return HttpResponse('This is from the product app view')
    products=Product.objects.all() # get in all to get single values
   
    context={
        'products':products,
    }

    return render(request,'product/index.html',context)

# to show category
@login_required
@admin_only
def show_category(request):
    category=Category.objects.all()
    context={
        'category':category,
    }

    return render(request,'product/showcategory.html',context)

@login_required
@admin_only
def post_product(request):
    # to insert products
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
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

@login_required
@admin_only
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

# To delete category 
@login_required
@admin_only
def delete_category(request,category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,'category deleted')
    return redirect('/product/showcategory')

# To delete product 
@login_required
@admin_only
def delete_product(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'product deleted')
    return redirect('/product')

# to edit category 
@login_required
@admin_only
def update_category(request,category_id):
    instance=Category.objects.get(id=category_id)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Category updated')
            return redirect('/product/showcategory')
        else:
            messages.add_message(request,messages.ERROR,'please validate')
            return render(request,'/product/showcategory.html',{'forms':form})
    context={
        'forms':CategoryForm(instance=instance)
    }
    return render(request,'product/updatecategory.html',context)

# to edit product 
@login_required
@admin_only
def update_product(request,product_id):
    instance=Product.objects.get(id=product_id)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'poroduct Updated')
            return redirect('/product')
        else:
            messages.add_message(request,messages.ERROR,'please validate')
            return render(request,'/product/index.html',{'forms':form})
    context={
        'forms':ProductForm(instance=instance)
    }
    return render(request,'product/updateproduct.html',context)