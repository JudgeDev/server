from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Views for the lists app
def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")
