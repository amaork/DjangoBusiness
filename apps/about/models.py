# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from ..core.models import Project, Document, NavigationModel


__all__ = ['CompanyInfo', 'ContactInfo']


class CompanyInfo(NavigationModel):
    """
    公司信息
    """
    url = 'about'
    text = "关于"
    sequence = 1

    name = models.CharField('公司名称', max_length=32)
    desc = models.TextField('公司简介', max_length=512)
    value = models.TextField('价值理念', max_length=512)
    comment = models.TextField('用户评价', max_length=512)
    logo = models.ForeignKey(Document, help_text='公司 LOGO', related_name='comp_logo', blank=True, null=True)


class ContactInfo(models.Model):
    """
    联系信息
    """
    name = models.CharField('名称', max_length=32)
    phone = models.CharField('电话', max_length=64, default='')
    email = models.EmailField('邮箱', default='')
    qq = models.CharField('QQ', max_length=16)
    weibo = models.CharField('微薄', max_length=32, default='')
    wechat = models.CharField('微信', max_length=16,  default='')
    address = models.CharField('地址', max_length=128, default='')
    qr_code = models.ForeignKey(Document, help_text='微信二维码', related_name='wechat', blank=True, null=True)

    def save(self, *args, **kwargs):
        if len(Project.objects.all()):
            Project.objects.update(phone=self.phone, address=self.address)
        super(ContactInfo, self).save(*args, **kwargs)
