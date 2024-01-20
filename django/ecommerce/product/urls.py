from django.urls import path
from .views import index,post_product,post_category

urlpatterns = [
    path('',index),
    path('addproduct/',post_product),
    path('addcategory/',post_category),
]