from django.contrib import admin

from blog.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


# register blog models with the admin classes
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
