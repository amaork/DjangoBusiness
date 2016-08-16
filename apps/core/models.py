# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import string


__all__ = ['Project', 'Document', 'NavigationBar', 'get_sequence_choices']


def get_sequence_choices(size):
    if size > len(string.digits):
        size = len(string.digits)

    return zip(str(string.digits[:size]), range(size))


class Project(models.Model):
    """
    核心 Model 首先需要创建一个 Project
    """
    HOMEPAGE_URL = 'homepage'

    name = models.CharField('名称', max_length=16)
    phone = models.CharField('电话', max_length=64, default='')
    email = models.EmailField('邮箱', default='')
    qq = models.CharField('QQ', max_length=16)
    weibo = models.CharField('微薄', max_length=32, default='')
    wechat = models.CharField('微信', max_length=16,  default='')
    address = models.CharField('地址', max_length=128, default='')

    qr_code = models.ForeignKey('Document', help_text='微信二维码', related_name='wechat')
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
        # 创建 Project 的时候自动创建主页导航
        for item in NavigationBar.objects.all():
            if item.url == self.HOMEPAGE_URL:
                break
        else:
            NavigationBar.objects.create(text='主页', url=self.HOMEPAGE_URL, sequence=0)

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
