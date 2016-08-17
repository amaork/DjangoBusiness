# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import string

__all__ = ['NavigationModel', 'Project', 'Document', 'NavigationBar', 'get_sequence_choices']


def get_sequence_choices(size):
    if size > len(string.digits):
        size = len(string.digits)

    return zip(str(string.digits[:size]), range(size))


class NavigationModel(models.Model):
    """
    继承 NavigationModel 后，定义 url, text, sequence 在保存模块的时候将会自动创建 NavigationBar Instance
    """
    url = ""
    text = ""
    sequence = -1

    def save(self, *args, **kwargs):
        if len(self.text) and len(self.url) and self.sequence != -1:
            if not NavigationBar.objects.filter(url=self.url, text=self.text):
                NavigationBar.objects.create(text=self.text, url=self.url, sequence=self.sequence)
        super(NavigationModel, self).save(*args, **kwargs)


class Project(NavigationModel):
    """
    核心 Model 首先需要创建一个 Project Instance，成功保存之后将自动完成一下动作：
    1. 创建 core.CompanyInfo 保存名称信息
    2. 创建 core.ContactInfo 保存电话与地址信息
    3. 创建 主页和关于页面的导航栏(NavigationBar)
    """
    text = "主页"
    sequence = 0
    url = 'homepage'

    name = models.CharField('名称', max_length=16)
    phone = models.CharField('电话', max_length=64, default='')
    address = models.CharField('地址', max_length=128, default='')
    cover = models.ForeignKey('Document', help_text='主页封面', related_name='cover')
    ico = models.ForeignKey('Document', help_text='浏览器 ICO', related_name='ico')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """保存 Project model instance 的时候自动创建 homepage 导航栏目

        :param args:
        :param kwargs:
        :return:
        """
        from ..about.models import CompanyInfo, ContactInfo

        # 自动创建 CompanyInfo
        if len(CompanyInfo.objects.all()) == 0:
            CompanyInfo.objects.create(name=self.name)
        else:
            CompanyInfo.objects.update(name=self.name)

        # 自动复制电话地址信息到 ContactInfo Model
        if len(ContactInfo.objects.all()) == 0:
            ContactInfo.objects.create(name=self.name, phone=self.phone, address=self.address)
        else:
            ContactInfo.objects.update(phone=self.phone, address=self.address)

        super(Project, self).save(*args, **kwargs)


class Document(models.Model):
    """
    文件 Model 负责上传存储各种类型的文件数据
    """
    name = models.CharField(max_length=32)
    docfile = models.FileField(upload_to="documents/%Y/%m/%d")

    def __str__(self):
        return self.name

    def url(self):
        return self.docfile.url

    def file_path(self):
        return self.docfile.name


class NavigationBar(models.Model):
    """
    导航栏
    """
    MAX_ITEM = 5
    SEQ_CHOICES = get_sequence_choices(MAX_ITEM)

    text = models.CharField("名称", max_length=16)
    url = models.CharField("地址", max_length=64)
    sequence = models.CharField('顺序', max_length=1, choices=SEQ_CHOICES)

    def __str__(self):
        return self.text
