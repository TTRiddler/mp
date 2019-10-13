from django import template
from datetime import datetime, timedelta
from os import name as os_name

register = template.Library()

time_format = '%#H:%M' if os_name == 'nt' else '%-H:%M'

@register.filter(name='custom_date')
def custom_date(value):
    if value.date() == datetime.today().date():
        value = 'сегодня ' + value.strftime(time_format)
    elif value.date() + timedelta(1) == datetime.today().date():
        value = 'вчера ' + value.strftime(time_format)
    else:
        value = value.strftime('%d.%m.%Y ' + time_format)
    return value