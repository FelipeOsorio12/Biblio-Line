from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from store_root.models.root import Root
from django.views import View


class LoginRoot(View):
    return_url = None

    def get(self, request):
        LoginRoot.return_url = request.GET.get ('return_url')
        return render (request, 'login_root.html')

    def post(self, request):
        username = request.POST.get ('username')
        password = request.POST.get ('password')

        root_password = Root.get_root()
        if password == root_password.password and username == 'root@gmail.com':
            return render(request, 'root.html')
        else:
            return render(request, 'login_root.html', {'error' : "Invalid"})

def logout_root(request):
    request.session.clear()
    return redirect('homepage')

