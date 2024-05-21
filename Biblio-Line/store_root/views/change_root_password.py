'''Module for managment password'''
import string
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.views import  View
from store_root.models.root import Root


class ChangeRootPassword(View):
    '''change pass view'''
    def get(self, request):
        '''get the view for change password'''
        return render(request, "change_root_password.html")

    def post(self, request):
        '''confirm change password data'''
        postData = request.POST
        old_password = postData.get('old_password')
        new_password = postData.get('new_password')
        confirm_password = postData.get('confirm_password')

        root_password = Root.get_root()

        if old_password == root_password.password and new_password == confirm_password:
            root_password.change_password(new_password)
            return render(request, 'change_root_password.html', {'good' : 'password was changed'} )
        else:
            return render(request, 'change_root_password.html', {'error' : 'Invalid'})


        
