from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=255,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class  Product(models.Model):
    product_name=models.CharField(max_length=255)
    product_price=models.FloatField()
    stock=models.IntegerField()
    product_description=models.TextField()
    product_image=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.product_name
