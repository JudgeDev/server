from django.contrib import admin

from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    pass


# register blog models with the admin classes
admin.site.register(Project, ProjectAdmin)
