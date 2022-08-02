from typing import Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from projects.models import Project

# Create your views here


def project_index(request: HttpRequest) -> HttpResponse:
    projects = Project.objects.all()  # query all projects
    context: Dict[str, str] = {"projects": projects}
    return render(request, "projects_index.html", context)


def project_detail(request: HttpRequest, pk: int) -> HttpResponse:
    project = Project.objects.get(pk=pk)
    context: Dict[str, str] = {"project": project}
    return render(request, "project_detail.html", context)
