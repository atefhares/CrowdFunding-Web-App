from django import template

register = template.Library()


@register.simple_tag
def div(n1, n2):
    return n1 / n2


@register.simple_tag
def mult(n1, n2):
    return n1 * n2


@register.simple_tag
def tround(n, by):
    return round(n, by)


@register.simple_tag
def percent_amount(n1, n2):
    return round(n1 / n2 * 100, 2)


@register.simple_tag
def subtract_date(n1, n2):
    calc = n1 - n2
    return calc.days


register.filter('mult', mult)
register.filter('round', tround)
register.filter('percent_amount', percent_amount)
register.filter('subtract_date', subtract_date)
