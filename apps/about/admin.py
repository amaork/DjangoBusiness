# -*- coding: utf-8 -*-
from django.contrib import admin, messages

from ..homepage.admin import OrderedModelAdmin
from .models import *


class AboutUsAdmin(OrderedModelAdmin):
    limit = 1
    list_display = ['name']


admin.site.register(AboutUs, AboutUsAdmin)
