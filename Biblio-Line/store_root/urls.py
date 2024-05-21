from django.contrib import admin
from django.urls import path
from .views.root import AddAdministrator
from .views.login_root import LoginRoot, logout_root
from .views.change_root_password import ChangeRootPassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('root_account', AddAdministrator.as_view(), name='root_account'),
    path('root_password', ChangeRootPassword.as_view(), name = 'root_password' ),
    path('logout_root', logout_root , name='logout_root'),

]
