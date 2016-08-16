# -*- coding: utf-8 -*-
from django.contrib import admin, messages

from .models import *


class OrderedModelAdmin(admin.ModelAdmin):
    limit = 1
    actions = ['swap_sequence',
               'move_sequence_up', 'move_sequence_down',
               'move_sequence_top', 'move_sequence_bottom']

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= self.limit:
            return False
        else:
            return True

    def swap_sequence(self, request, queryset):
        if len(queryset.all()) != 2:
            self.message_user(request, "swap action needs two items!", messages.WARNING)
        else:
            item1 = queryset.all()[0]
            item2 = queryset.all()[1]
            item1.sequence, item2.sequence = item2.sequence, item1.sequence
            item1.save()
            item2.save()
            self.message_user(request, "Select items sequence has swap")

    @staticmethod
    def update_sequence(item, sequence):
        item.sequence = str(sequence)
        item.save()

    def move_sequence_up(self, request, queryset):
        for item in queryset.all():
            if item.sequence != '0':
                self.update_sequence(item, int(item.sequence) - 1)

        self.message_user(request, "Select item sequence has move up")

    def move_sequence_down(self, request, queryset):
        for item in queryset.all():
            if item.sequence != str(self.limit - 1):
                self.update_sequence(item, int(item.sequence) + 1)

        self.message_user(request, "Select item sequence has move down")

    def move_sequence_top(self, request, queryset):
        if len(queryset.all()) != 1:
            self.message_user(request, "Move top action only support 1 item", messages.WARNING)
        else:
            self.update_sequence(queryset.all()[0], 0)
            self.message_user(request, "Select item sequence has move to top")

    def move_sequence_bottom(self, request, queryset):
        if len(queryset.all()) != 1:
            self.message_user(request, "Move bottom action only support 1 item", messages.WARNING)
        else:
            self.update_sequence(queryset.all()[0], self.limit - 1)
            self.message_user(request, "Select item sequence has move to bottom")


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
