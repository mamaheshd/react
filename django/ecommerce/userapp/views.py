from django.shortcuts import render,redirect
from product.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import LoginForm

# Create your views here.
def index(request):
    products=Product.objects.all().order_by('-id')[:8]
    context={
        'products':products
    }
    return render(request,'user/index.html',context)

def product_details(request,product_id):
    product=Product.objects.get(id=product_id)
    context={
        'product':product
    }
    return render(request,'user/productdetails.html',context)

def products(request):
    products=Product.objects.all().order_by('-id')
    context={
        'products':products
    }
    return render(request,'user/products.html',context)

# to register User
def register_user(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'New account created')
            return redirect('/register')
        else:
            messages.add_message(request,messages.ERROR,'please verify forms fields')
            return render(request,'user/register.html',{'forms':form})
    context={
        'forms':UserCreationForm
    }
    return render(request,'user/register.html',context)

#login process
def user_login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
              messages.add_message(request,messages.ERROR,'Please provide correct Credentials')
              return render(request,'user/login.html',{'forms':form})  
    context={
        'forms':LoginForm
    }
    return render(request,'user/login.html',context)