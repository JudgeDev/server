from typing import Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here


# from projects.models import Project


def project_index(request: HttpRequest) -> HttpResponse:
    # projects = Project.objects.all()
    context: Dict[str, str] = {}
    # context = {
    #    'projects': projects
    # }
    return render(request, "projects_index.html", context)
