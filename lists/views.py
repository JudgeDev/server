# from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Views for the lists app
def home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<html><title>To-Do lists</title></html>")
