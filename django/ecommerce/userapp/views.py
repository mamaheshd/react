from django.shortcuts import render,redirect
from product.models import Product,Cart
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

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
                if user.is_staff:
                    return redirect('/admin/dashboard')
                else:
                    return redirect('/')
            else:
              messages.add_message(request,messages.ERROR,'Please provide correct Credentials')
              return render(request,'user/login.html',{'forms':form})  
    context={
        'forms':LoginForm
    }
    return render(request,'user/login.html',context)

#logout 
def logout_user(request):
    logout(request)
    return redirect('/login')

@login_required
def add_to_cart(request,product_id):
    users=request.user
    products=Product.objects.get(id=product_id)

    check_item_presence=Cart.objects.filter(user=users,product=products) # user and product is from model Cart
    if check_item_presence:
        messages.add_message(request,messages.ERROR,'Product is already inn the cart')
        return redirect('/cart')
    else:
        cart=Cart.objects.create(product=products,user=users)
        if cart:
            messages.add_message(request,messages.SUCCESS,'Product is add to cart')
            return redirect('/cart')
        else:
            messages.add_message(request,messages.ERROR,'Failed to add product in cart')
            return redirect('/cart')
        
@login_required
def show_user_cart_items(request):
    users=request.user
    items=Cart.objects.filter(user=users)
    context={
        'items':items
    }
    return render(request,'user/cart.html',context)

@login_required
def remove_cart(request,cart_id):
    cart=Cart.objects.get(id=cart_id)
    cart.delete()
    messages.add_message(request,messages.SUCCESS,'Item remove from the cart')
    return redirect('/cart')