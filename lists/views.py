""" Views for lists app

Views should process user input and return appropriate response.

Views look like "normal" Django views:
They take information from a user's request,
combine it with some custom logic or information from the URL (list_id),
pass it to a form for validation and possible saving,
and then redirect or render a template.

Thin views:
If views are too complex with a lot of tests for them,
check whether logic could be moved elsewhere
- possibly to a form
- or to a custom method on the model class
- or if complexity of app demands it, out of Django into own classes.
"""

# from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from lists.forms import ExistingListItemForm, ItemForm
from lists.models import List


# Views for the lists app
def home_page(request: HttpRequest) -> HttpResponse:
    """Home page view"""
    # use form for Item
    return render(request, "home.html", {"form": ItemForm()})


def view_list(request: HttpRequest, list_id: int) -> HttpResponse:
    """View an existing todo list"""
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == "POST":
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            # Avoid: Item.objects.create(text=request.POST["text"], list=list_)
            form.save()  # ...by using custom save
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
        # Avoid: Item.objects.create(text=request.POST["text"], list=list_)
        form.save(for_list=list_)  # ...by using custom save to save form
        # instead of return redirect(f"/lists/{list_.id}/")
        return redirect(list_)  # ...use url resolution
    else:
        # pass form to template instead of hardcoded error
        return render(request, "home.html", {"form": form})
