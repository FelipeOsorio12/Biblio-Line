from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.customer import Customer
from store.models.product import Products
from store.models.orders import Order

class Refound(View):
    def post(self, request):
        order_id = request.POST.get('.refund-btn')
        print (f"order --{order_id}")
        return redirect('orders')
