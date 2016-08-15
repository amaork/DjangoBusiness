# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'wechat', 'phone', 'address')

    def has_add_permission(self, request):
        # 只允许创建一个 Project Model instance
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


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


class NavigationBarAdmin(admin.ModelAdmin):
    list_filter = ['sequence']
    search_fields = ['text', 'url']
    list_display = ('text', 'url', 'sequence')


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(HeaderItem, HeaderItemAdmin)
admin.site.register(ArticleItem, ArticleItemAdmin)
admin.site.register(NavigationBar, NavigationBarAdmin)
