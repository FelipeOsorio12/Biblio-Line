'''Module for the order view'''
from django.shortcuts import render
from django.views import View
from store.models.orders import Order


class OrderView(View):
    '''class for the order view'''
    def get(self , request ):
        '''get the view'''
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        return render(request , 'orders.html'  , {'orders' : orders})
    

    
