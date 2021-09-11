from crum import get_current_user
from django import template

from users.models import User

register = template.Library()


@register.filter(name='get_current_user')
def get_current_user(request=None):
    user = None
    if not request:
        user = get_current_user()
    elif request.user.is_authenticated:
        user = request.user
    if user:
        user = User.objects.filter(user=user).first()
    return user


@register.filter(name='get_different_parameters')
def get_different_parameters(request, current_parameter):
    params = dict(request.GET)
    args_str = ''
    excluded_args = ['page', current_parameter]
    last_symbol_arg = '?'
    for arg, value in params.items():
        if isinstance(value, list):
            value = value[0]
        if arg not in excluded_args and value:
            if args_str:
                args_str += f'{last_symbol_arg}{arg}={value}'
            else:
                args_str = f'{last_symbol_arg}{arg}={value}'
                last_symbol_arg = '&'
    args_str = args_str + last_symbol_arg
    return args_str
