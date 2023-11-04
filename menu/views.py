from django.shortcuts import render

from .models import MenuItem


def menu_items_view(request, pk=None):
    menu_items = MenuItem.objects.all()
    if pk:
        selected_item = menu_items.get(id=pk)
        menu_dict = selected_item.build_nested_dict_to_parent()
    else:
        menu_dict = None
    return render(request, 'item_detail.html', {'menu_dict': menu_dict,
                                                'menu_items': menu_items})
