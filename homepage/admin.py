from django.contrib import admin

from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'wechat', 'phone', 'address')


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_path', 'url')


class HeaderItemAdmin(admin.ModelAdmin):
    list_filter = ['sequence']
    search_fields = ['title', 'abstract', 'context']
    list_display = ('title', 'sequence')


class ArticleItemAdmin(admin.ModelAdmin):
    fieldsets = [

        (None, {'fields': ['title', 'title2', 'abstract', 'context', 'sequence', 'cover']}),

    ]
    list_filter = ['sequence']
    search_fields = ['title', 'abstract', 'context']
    list_display = ('title', 'title2', 'sequence',)


class NavigationItemAdmin(admin.ModelAdmin):
    list_filter = ['sequence']
    search_fields = ['text', 'url']
    list_display = ('text', 'url', 'sequence')


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(HeaderItem, HeaderItemAdmin)
admin.site.register(ArticleItem, ArticleItemAdmin)
admin.site.register(NavigationItem, NavigationItemAdmin)
