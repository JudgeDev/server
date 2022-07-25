""" Views for lists app

Views should process user input and return appropriate response.
"""

# from django.core.exceptions import ValidationError
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
    form = ItemForm()
    # error = None
    if request.method == "POST":
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST["text"], list=list_)
            # redirect to same form that POST request came from
            # using url resolution
            return redirect(list_)
    # render request with list template and table items and form
    # insted of errors
    return render(request, "list.html", {"list": list_, "form": form})


def new_list(request: HttpRequest) -> HttpResponse:
    form = ItemForm(data=request.POST)  # pass request.POST data to form
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST["text"], list=list_)
        # instead of return redirect(f"/lists/{list_.id}/")
        return redirect(list_)  # ...use url resolution
    else:
        # pass form to template instead of hardcoded error
        return render(request, "home.html", {"form": form})
