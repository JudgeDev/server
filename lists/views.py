""" Views for lists app

Views should process user input and return appropriate response.
"""

from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item, List


# Views for the lists app
def home_page(request: HttpRequest) -> HttpResponse:
    """Home page view"""
    return render(request, "home.html")


def view_list(request: HttpRequest, list_id: int) -> HttpResponse:
    """View an existing todo list"""
    list_ = List.objects.get(id=list_id)
    if request.method == "POST":
        Item.objects.create(text=request.POST["item_text"], list=list_)
        # redirect to same form that POST request came from
        return redirect(f"/lists/{list_.id}/")
    # render request with list template and table items
    return render(request, "list.html", {"list": list_})


def new_list(request: HttpRequest) -> HttpResponse:
    list_ = List.objects.create()
    item = Item(text=request.POST["item_text"], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, "home.html", {"error": error})
    return redirect(f"/lists/{list_.id}/")
