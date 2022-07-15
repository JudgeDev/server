""" Views for lists app

Views should process user input and return appropriate response.
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item, List


# Views for the lists app
def home_page(request: HttpRequest) -> HttpResponse:
    """Home page view"""
    return render(request, "home.html")


def view_list(request: HttpRequest) -> HttpResponse:
    """View an existing todo list"""
    items = Item.objects.all()  # get all table items
    # render request with home template and table items
    return render(request, "list.html", {"items": items})


def new_list(request: HttpRequest) -> HttpResponse:
    list_ = List.objects.create()
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect("/lists/the-only-list-in-the-world/")
