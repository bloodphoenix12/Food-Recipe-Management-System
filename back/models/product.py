from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    Ingredients = models.CharField(max_length=800, blank=True, null=True)
    Instructions = models.CharField(max_length=800, blank=True, null=True)
    time = models.IntegerField(default=0)

    category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/',blank=True, null=True)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();