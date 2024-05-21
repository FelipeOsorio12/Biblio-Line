'''Module for the customer account'''
import string
from geonamescache import GeonamesCache
from store.models.customer import Customer
from django.shortcuts import render, redirect
from django.views import View

class Account (View):
    '''view class for the account service'''
    def get(self, request):
        '''get function for bring the account data'''
        id = request.session.get('customer')

        customer = Customer.get_customer_by_id(id)
        g_c = GeonamesCache()
        #get country list
        countries = g_c.get_countries()

        data = {
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'phone': customer.phone,
            'email': customer.email,
            'date' : customer.date,
            'address': customer.address,
            'country':customer.country,
            'description' : customer.description
        }

        return render (request, 'account.html', data)

    def post(self, request):
        '''post function for manipulate account data'''
        postData = request.POST
        first_name = postData.get ('firstname')
        last_name = postData.get ('lastname')
        phone = postData.get ('phone')
        email = postData.get ('email')
        description = postData.get('description')
        address = postData.get('address')

                # validation
        data = (
            first_name,
            last_name,
            phone,
            email,
            address,
            description
        )

        id = request.session.get('customer')

        customer = Customer.get_customer_by_id(id)
        customer.update(data)

        return redirect('homepage')

    def validateCustomer(self, customer, confirm):
        '''validate if a customer exists or not'''
        error_message = None
        if not customer.first_name:
            error_message = "Please Enter your First Name !!"
        elif len (customer.first_name) < 3:
            error_message = 'First Name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please Enter your Last Name'
        elif len (customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your Phone Number'
        elif len (customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len (customer.password) < 7:
            error_message = 'Password must be 7 char long'
        elif not any([char.isdigit() for char in customer.password]):
            error_message = 'Password requires a digit'
        elif not any([char.isupper() for char in customer.password]):
            error_message = 'Password requires a capital'
        elif not any([True if char in string.punctuation else False for char in customer.password]):
            error_message = 'Password requires a special character' 
        elif len (customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists ():
            error_message = 'Email Address Already Registered..'
        elif customer.password != confirm:
            error_message  = 'The passwords do not match'

        # saving

        return error_message
