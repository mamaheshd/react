from django.db import models

class  Product(models.Model):
    product_name=models.CharField(max_length=255)
    product_price=models.FloatField()
    stuck=models.IntegerField()
    product_description=models.TextField()
    product_image=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)

