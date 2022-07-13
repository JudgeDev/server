""" Views for lists app

Views should process user input and return appropriate response.
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item


# Views for the lists app
def home_page(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        # create and store new item with POST contents
        Item.objects.create(text=request.POST["item_text"])
        return redirect("/")
    items = Item.objects.all()  # get all table items
    # render request with home template and table items
    return render(request, "home.html", {"items": items})
