# -*- coding: utf-8 -*-
from django.contrib import admin

from ..core.admin import LimitInstanceAdmin
from .models import *


class CompanyInfoAdmin(LimitInstanceAdmin):
    limit = 1
    list_display = ['name']
    fields = ('name', 'desc', 'value', 'comment', 'logo', 'self_define_cover')


class ContactInfoAdmin(LimitInstanceAdmin):
    limit = 1
    list_display = ['name', 'wechat', 'phone', 'email', 'address']
    fields = ('name', 'phone', ('wechat', 'qr_code'), 'email', 'qq', 'weibo', 'address', 'self_define_cover')


class CommentMessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'name', 'wechat', 'phone', 'comment']


admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(CommentMessage, CommentMessageAdmin)
