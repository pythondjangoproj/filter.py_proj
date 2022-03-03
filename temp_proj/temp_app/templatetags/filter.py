from django import template

register=template.Library()

def testing_filter(value):
    result=value[0:3]
    return result
register.filter('testing_filter',testing_filter)