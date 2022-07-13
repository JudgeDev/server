from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Views for the lists app
def home_page(request: HttpRequest) -> HttpResponse:
    # render request with given template and template variable dict
    return render(
        request,
        "home.html",
        {
            "new_item_text": request.POST.get("item_text", ""),
        },
    )
