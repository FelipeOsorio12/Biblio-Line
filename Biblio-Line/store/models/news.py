from django.db import models
from .product import Products


class News(models.Model):
    name = models.CharField(max_length=100)
    information = models.CharField(max_length=250)
    date_up = models.DateField()
    

    @staticmethod
    def get_all_news():
        '''Method for getting all products'''
        return News.objects.all()
    
    


    
