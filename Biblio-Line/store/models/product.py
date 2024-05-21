'''Class for products and books in the library'''
from django.db import models
from .category import Category

class Products(models.Model):
    '''Class for products and books in the library'''
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1 )
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='uploads/products/')
    author = models.CharField(max_length=150)
    date_publi = models.DateField()
    pages = models.IntegerField()
    publisher = models.CharField(max_length=60)
    language = models.CharField(max_length=60)
    state = models.CharField(max_length=15)

    @staticmethod
    def get_products_by_id(ids):
        '''Method for getting products by id'''
        return Products.objects.filter (id__in=ids)

    @staticmethod
    def get_all_products():
        '''Method for getting all products'''
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        '''Method for getting all products by category'''
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products()
