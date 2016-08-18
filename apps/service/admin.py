from django.contrib import admin
from .models import *
from ..core.admin import OrderedModelAdmin


class ServiceItemAdmin(OrderedModelAdmin):
    limit = ServiceItem.MAX_ITEM

    list_display = ['name', 'price', 'sequence']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['slogan']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
