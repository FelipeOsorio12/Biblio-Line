'''Module for the news added for the customer'''
from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Products
from store.models.news import News
from store.models.customer import Customer

class NewsViews(View):
    '''view class for the account service'''
    def get(self, request):
        '''get function for bring the account data'''
        customer = request.session.get('customer')
        subs = Customer.get_customer_by_id(customer)
        subs = subs.is_subscribed
        news = News.get_all_news()
        

        
        return render (request, 'news.html', {'news': news, 'customer' : customer, 'subs' : subs})
    
def Subscribe(request):
    customer = request.session.get('customer')
    customer = Customer.get_customer_by_id(customer)
    customer.tosubscribe()

    return redirect('news')
