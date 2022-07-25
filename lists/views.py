""" Views for lists app

Views should process user input and return appropriate response.
"""

from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from lists.forms import ItemForm
from lists.models import Item, List


# Views for the lists app
def home_page(request: HttpRequest) -> HttpResponse:
    """Home page view"""
    # use form for Item
    return render(request, "home.html", {"form": ItemForm()})


def view_list(request: HttpRequest, list_id: int) -> HttpResponse:
    """View an existing todo list"""
    list_ = List.objects.get(id=list_id)
    error = None
    if request.method == "POST":
        try:
            item = Item(text=request.POST["text"], list=list_)
            item.full_clean()
            item.save()
            # redirect to same form that POST request came from
            # using url resolution
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"
    # render request with list template and table items and any errors
    return render(request, "list.html", {"list": list_, "error": error})


def new_list(request: HttpRequest) -> HttpResponse:
    list_ = List.objects.create()
    item = Item(text=request.POST["text"], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, "home.html", {"error": error})
    # return redirect(f"/lists/{list_.id}/") using url resolution
    return redirect(list_)
