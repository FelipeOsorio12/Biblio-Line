'''Custom filters'''
from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    '''Return a int value with the currency of dollar'''
    return "$" + str(number)

@register.filter(name='multiply')
def multiply(number , number1):
    '''Return multiply of a two numbers'''
    return number * number1
