from django.shortcuts import render
from .models import Item
from django.http import Http404

# Create your views here.
def item_list(request, item_id):
    item = Item.objects.get(pk= item_id)
    if item is not None:
        return render(request, 'item/item_list.html', {'Item': Item })

    else:
        raise Http404('Item Does Not Exist')


def instock(request, instock_id):
    instock = Item.objects.get(pk= instock_id)
    if instock is not None:
        return render(request, 'selection/instock.html', {'': instock})

    else:
        raise Http404('Item No Longer Available')

