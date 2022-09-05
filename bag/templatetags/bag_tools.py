from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    '''
    Returns and renders the subtotal for each item in bag:
    When update option is clicked
    '''
    return price * quantity
