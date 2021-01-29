from django import template
#from store.models.product import Product

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return str(number)+" XOF"


@register.filter(name='multiply')
def multiply(number, number1):
    return number * number1
