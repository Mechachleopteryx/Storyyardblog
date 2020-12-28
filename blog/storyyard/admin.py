from django.contrib import admin
from .models import BLOG, COMMENT, Category


class BLOGADMIN(admin.ModelAdmin):
    list_display = ('title', 'published', 'category', 'time', 'date')


class COMMENTADMIN(admin.ModelAdmin):
    list_display = ('author', 'email', 'created')


admin.site.register(BLOG, BLOGADMIN)
admin.site.register(COMMENT, COMMENTADMIN)
admin.site.register(Category)
