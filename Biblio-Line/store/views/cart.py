'''Module for the customer cart'''
from django.shortcuts import render
from django.views import  View
from store.models.product import Products
from store.models.customer import Customer 
from geonamescache import GeonamesCache
from store.models.shop import Shop


class Cart(View):
    '''view class for cart products'''
    def get(self , request):
        '''get all products inside the cart'''
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        id = request.session.get('customer')
        customer = Customer.get_customer_by_id(id)
        shops = Shop.objects.all()

        print(customer.first_name)
        print(products)

        value = {
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'phone': customer.phone,
            'email': customer.email,
            'address': customer.address,
            'country': customer.country,
            'city': customer.city,
            'products' : products ,
            'shops': shops,
            #'countries': countries
        }

        g_c = GeonamesCache()
        countries = g_c.get_countries()
        return render(request , 'cart.html' , value )
