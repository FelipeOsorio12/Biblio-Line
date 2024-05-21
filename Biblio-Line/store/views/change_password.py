'''Module for managment password'''
import string
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.views import  View
from store.models.customer import Customer


class ChangePassword(View):
    '''change pass view'''
    def get(self, request):
        '''get the view for change password'''
        return render(request, "change_password.html")

    def post(self, request):
        '''confirm change password data'''
        postData = request.POST
        old_password = postData.get('old_password')
        new_password = postData.get('new_password')
        confirm_password = postData.get('confirm_password')

        id = request.session.get('customer')
        customer = Customer.get_customer_by_id(id)
        checkpassword= check_password(old_password, customer.password)
        checkpassword2= check_password(new_password, customer.password)

        if checkpassword and not checkpassword2:
            error_message = self.validateCustomer(new_password, confirm_password)

            if not error_message:
                print(old_password)
                print(new_password)
                print(confirm_password)

                new_password = make_password (new_password)
                customer.change_password(new_password)

                return render(request, 'change_password.html', {'good': 'The password was changed successfully'})
            else:
                data = {
                    'error': error_message,
                }

                return render (request, 'change_password.html', data)
        else:
            error_message = 'old password invalid or old and new password are same'
            data={
                'error': error_message
            }
            return render (request, 'change_password.html', data)

    def validateCustomer(self, new, confirm):
        '''validate customer account'''
        error_message = None
        if len (new) < 7:
            error_message = 'Password must be 7 char long'
        elif not any([char.isdigit() for char in new]):
            error_message = 'Password requires a digit'
        elif not any([char.isupper() for char in new]):
            error_message = 'Password requires a capital'
        elif not any([True if char in string.punctuation else False for char in new]):
            error_message = 'Password requires a special character' 
        elif new != confirm:
            error_message  = 'The passwords do not match'
        # saving
        return error_message
