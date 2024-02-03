from django.shortcuts import render,redirect
# from product.models import Product,Cart,Order
from product.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from product.forms import OrderForm


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

@login_required #decorators
def post_order(request,product_id,cart_id):
    user=request.user
    product=Product.objects.get(id=product_id)
    cart_item=Cart.objects.get(id=cart_id)
    
    if request.method == 'POST':
        form =OrderForm(request.POST)
        if form.is_valid():
            quantity=request.POST.get('quantity')
            price=product.product_price
            total_price=int(quantity)*int(price)
            contact_no=request.POST.get('contact_no')
            address= request.POST.get('address')
            payment_method=request.POST.get('payment_method')
            payment_status=request.POST.get('payment_status')
            # to create an order
            order=Order.objects.create(
                product=product,
                user=user,
                quantity=quantity,
                total_price=total_price,
                contact_no=contact_no,
                address=address,
                payment_method=payment_method,
                payment_status=payment_status
            )
            if order.payment_method == 'Cash on Delivery':
                cart_item.delete()
                messages.add_message(request,messages.SUCCESS,'order sucessfull')
                return redirect('/myorder')
            elif order.payment_method == 'Esewa':
                context ={
                    'order':order,
                    'cart':cart_item
                }
                return render(request,'user/esewa_payment.html',context)
            else:
                messages.add_message(request,messages.ERROR,'Failed to make order')
                return render(request,'user/orderform.html',{'forms':form})

    context={
        'forms':OrderForm
    }
    return render(request,'user/orderform.html',context)

import requests as req
def esewa_verify(request):
    import xml.etree.ElementTree as ET

    o_id=request.GET.get('pid')
    amount=request.GET.get('amt')
    refId=request.GET.get('refId')
    url ="https://uat.esewa.com.np/epay/transrec"
    d = {
    'amt': amount,
    'scd': 'EPAYTEST',
    'rid': refId,
    'pid':o_id,
    }
    resp = req.post(url, d)
    root=ET.fromstring(resp.content)
    status=root[0].text.strip()
    if status == 'Success':
        order_id=o_id.split("_")[0]
        order=Order.objects.get(id=order_id)
        order.payment_status=True
        order.save()
        #cart
        cart_id=o_id.split("_")[1]
        cart=Cart.objects.get(id=cart_id)
        cart.delete()
        messages.add_message(request,messages.SUCCESS,'Payment successful')
        return redirect('/cart')
    else:
        messages.add_message(request,messages.ERROR,'Unable to make payment')
        return redirect('/cart')

@login_required
def my_order(request):
    user=request.user
    items=Order.objects.filter(user=user)
    context={
        'items':items
    }
    return render(request,'user/myorder.html',context)