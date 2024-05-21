import string
from geonamescache import GeonamesCache
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views import View
from store.models.customer import Customer



class Signup(View):

    def get(self, request):
        g_c = GeonamesCache()
        #get country list
        countries = g_c.get_countries()
        return render(request, 'signup.html',{'countries': countries})

    def post(self, request):
        post_data = request.POST
        first_name = post_data.get ('firstname')
        last_name = post_data.get ('lastname')
        phone = post_data.get ('phone')
        email = post_data.get ('email')
        password = post_data.get ('password')
        confirmpassword = post_data.get('confirmpassword')
        date = post_data.get('date')
        address = post_data.get('address')
        country_id = post_data.get('country')
        city_id = post_data.get('city')
        print(country_id)
        print(city_id)

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
            'password': password,
            'date' : date,
            'address': address,
            'country': country_id,
            'city': city_id
        }

        error_message = None

        customer = Customer (first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password,
                             date = date,
                             address = address,
                             country = country_id,
                             city = city_id)

        error_message = self.validateCustomer(customer, confirmpassword)

        if not error_message:
            print (first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }

            g_c = GeonamesCache()
            countries = g_c.get_countries()
            data['countries'] = countries

            return render (request, 'signup.html', data)

    def validateCustomer(self, customer, confirm):
        print(customer)
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

    def get_cities_by_country(self, country_code):
        # Cargar todas las ciudades desde la API
        g_c = GeonamesCache()
        cities = g_c.get_cities()

        # Filtrar las ciudades por país
        cities_for_country = [city_data for city_data in cities.values() if city_data['countrycode'] == country_code]

        # Crear el HTML para el select de ciudades
        select_html = '<select name="city" id="city">'
        select_html += '<option value="">Select a city</option>'
        for city in cities_for_country:
            select_html += f'<option value="{city["geonameid"]}">{city["name"]}</option>'
        select_html += '</select>'

        return select_html

class CitiesByCountry(View):
    def get_cities_by_country(self, country_code):
        # Obtener el HTML para el select de ciudades del país seleccionado
        signup = Signup()
        select_html = signup.get_cities_by_country(country_code)
        # Devolver el HTML como respuesta HTTP
        return HttpResponse(select_html)
