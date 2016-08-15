# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import *


class OrderedModelAdmin(admin.ModelAdmin):
    limit = 1
    actions = ['swap']

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= self.limit:
            return False
        else:
            return True

    def swap(self, request, queryset):
        if len(queryset.all()) != 2:
            self.message_user(request, "swap action needs two items!")
        else:
            item1 = queryset.all()[0]
            item2 = queryset.all()[1]
            item1.sequence, item2.sequence = item2.sequence, item1.sequence
            item1.save()
            item2.save()

    swap.short_description = "Swap two item sequence"


class ProjectAdmin(OrderedModelAdmin):
    list_display = ('name', 'wechat', 'phone', 'address')


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_path', 'url')


class HorizontalItemAdmin(OrderedModelAdmin):
    limit = HorizontalItem.MAX_ITEM

    list_filter = ['sequence']
    list_display = ('title', 'sequence')
    search_fields = ['title', 'abstract', 'context']


class VerticalItemAdmin(OrderedModelAdmin):
    fieldsets = [

        (None, {'fields': ['title', 'title2', 'abstract', 'sequence', 'cover']}),

    ]

    limit = VerticalItem.MAX_ITEM

    list_filter = ['sequence']
    search_fields = ['title', 'abstract', 'context']
    list_display = ('title', 'title2', 'sequence',)


class NavigationBarAdmin(OrderedModelAdmin):
    limit = NavigationBar.MAX_ITEM

    list_filter = ['sequence']
    search_fields = ['text', 'url']
    list_display = ('text', 'url', 'sequence')


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(VerticalItem, VerticalItemAdmin)
admin.site.register(NavigationBar, NavigationBarAdmin)
admin.site.register(HorizontalItem, HorizontalItemAdmin)
