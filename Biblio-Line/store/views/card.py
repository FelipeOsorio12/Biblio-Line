import string
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import  View
from store.models.customer import Customer
from store.models.card import Card
from store.models.shop import Shop

class CardViews(View):
    def get(self, request):

        return render(request, 'card.html')
    
    def post(self, request):
        return redirect("account")
