from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.news import News


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'author', 'date_publi', 'pages',
                    'publisher', 'language', 'state'
                    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'quantity', 'price', 'address','customer_id', 'product_id', 'pick']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

# Register your models here.
admin.site.register(Products, AdminProduct)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order,  OrderAdmin)
admin.site.register(News)


# username = admin  password = biblioline001
