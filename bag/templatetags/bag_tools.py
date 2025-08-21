from django import template


register = template.Library()  # register is a variable


@register.filter(name='calc_subtotal')  # using register filter decorator to register our function as a template filter
def calc_subtotal(price, quantity):  # price and quantity is a parameter
    return price * quantity
