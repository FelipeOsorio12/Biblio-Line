'''Module for the home page'''
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View
from store.models.product import Products
from store.models.category import Category
from store.models.news import News


class Index(View):
    '''Main page class'''
    def post(self , request):
        '''Render all view for homepage'''
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')

    def get(self , request):
        '''get store'''
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    '''store method'''
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    author = request.GET.get('author')
    news = News.get_all_news()
    
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    elif author:
        products = Products.objects.filter(author__icontains=author)
    else:
        products = Products.get_all_products()


    data = {}
    data['products'] = products
    data['categories'] = categories
    data['news'] = news

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)
