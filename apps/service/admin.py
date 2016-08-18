from django.contrib import admin
from .models import *
from ..core.admin import OrderedModelAdmin, LimitInstanceAdmin


class ServiceItemAdmin(OrderedModelAdmin):
    limit = ServiceItem.MAX_ITEM
    list_display = ['name', 'price', 'sequence']


class ServiceAdmin(LimitInstanceAdmin):
    list_display = ['slogan']
    fields = ("slogan", "self_define_cover")


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
