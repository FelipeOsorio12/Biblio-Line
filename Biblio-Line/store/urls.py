from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.signup import CitiesByCountry
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.change_password import ChangePassword
from .views.account import Account
from .views.news import NewsViews, Subscribe
from .views.refund import Refound
from .views.card import CardViews

from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('account', Account.as_view(), name = 'account'),
    path('change_password', ChangePassword.as_view(), name = "change_password"),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('get_cities_by_country/<str:country_code>/', CitiesByCountry.get_cities_by_country, name='get_cities_by_country'),
    path('news', NewsViews.as_view(), name = 'news'),
    path('refound', Refound.as_view(), name = 'refound'),
    path('subscribe', Subscribe, name = 'subscribe'),
     path('card', CardViews.as_view(), name = 'card'),
]
