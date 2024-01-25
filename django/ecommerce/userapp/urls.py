from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('productdetails/<int:product_id>',product_details),
    path('productlist/',products),
]