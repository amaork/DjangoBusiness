# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from ..core.models import Document, NavigationBar


class CompanyInfo(models.Model):
    URL = 'about'

    name = models.CharField('公司名称', max_length=32)
    desc = models.TextField('公司简介', max_length=1024)
    value = models.TextField('价值理念', max_length=1024)
    logo = models.ForeignKey(Document, help_text='公司 LOGO', related_name='comp_logo')

    def save(self, *args, **kwargs):
        """保存 AboutUs model instance 的时候自动创建 about 导航栏目

        :param args:
        :param kwargs:
        :return:
        """
        # 创建 Project 的时候自动创建关于导航
        for item in NavigationBar.objects.all():
            if item.url == self.URL:
                break
        else:
            NavigationBar.objects.create(text='关于', url=self.URL, sequence=1)

        super(CompanyInfo, self).save(*args, **kwargs)
