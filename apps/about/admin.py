# -*- coding: utf-8 -*-
from django.contrib import admin

from ..core.admin import LimitInstanceAdmin
from .models import *


class CompanyInfoAdmin(LimitInstanceAdmin):
    limit = 1
    list_display = ['name']


admin.site.register(CompanyInfo, CompanyInfoAdmin)
