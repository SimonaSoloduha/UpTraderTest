from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def draw_menu(menu_dict):
    if menu_dict is None:
        return ''

    result = '<ul>'
    for key, value in menu_dict.items():
        result += f'<li><a href="\\{value["id"]}">{key} - {value["id"]}</a>'
        if value["menu"]:
            result += draw_menu(value["menu"])
        result += '</li>'
    result += '</ul>'
    return mark_safe(result)


register.filter('draw_menu', draw_menu)
