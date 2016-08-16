# -*- coding: utf-8 -*-
from django.contrib import admin, messages
from .models import *

from ..core.admin import OrderedModelAdmin


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


# Register your models here.
admin.site.register(VerticalItem, VerticalItemAdmin)
admin.site.register(HorizontalItem, HorizontalItemAdmin)
