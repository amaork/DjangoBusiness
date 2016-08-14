# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import string


__all__ = ['Project', 'Document', 'HeaderItem', 'ArticleItem', 'NavigationItem']


def get_sequence_choice(size):
    if size > len(string.digits):
        size = len(string.digits)

    return zip(str(string.digits[:size]), range(size))


class Project(models.Model):
    UNIQUE = (
        ('U', 'Unique')
    )
    name = models.CharField('项目名称', max_length=16)
    email = models.EmailField('邮箱', default='')
    wechat = models.CharField('微信', max_length=16,  default='')
    qr_code = models.ForeignKey('Document', help_text='微信二维码', related_name='wechat')
    phone = models.CharField('联系电话', max_length=64, default='')
    address = models.CharField('联系地址', max_length=128, default='')
    cover = models.ForeignKey('Document', help_text='项目封面', related_name='cover')
    logo = models.ForeignKey('Document', help_text='项目图标', related_name='logo')
    unique = models.CharField('锁定', max_length=1, default='U', unique=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    name = models.CharField(max_length=32)
    docfile = models.FileField(upload_to="documents/%Y/%m/%d")

    def __str__(self):
        return self.name

    def url(self):
        return self.docfile.url

    def file_path(self):
        return self.docfile.name


class BaseArticle(models.Model):
    # 标题
    title = models.CharField('标题', max_length=64)

    # 概要
    abstract = models.CharField('摘要', max_length=128)

    # 详细内容
    context = models.TextField('正文', help_text='文章的正文内容')

    def __str__(self):
        return self.title


class HeaderItem(BaseArticle):
    MAX_ITEM = 3
    SEQ_CHOICES = get_sequence_choice(MAX_ITEM)

    # 显示顺序
    sequence = models.CharField('顺序', max_length=1, choices=SEQ_CHOICES, unique=True)

    # 图标
    cover = models.ForeignKey('Document', help_text='文章的封面图标')

    # def save(self, *args, **kwargs):
    #     super(HeaderItem, self).save(*args, **kwargs)


class NavigationItem(models.Model):
    MAX_ITEM = 5
    SEQ_CHOICES = get_sequence_choice(MAX_ITEM)

    text = models.CharField("名称", max_length=16)
    url = models.CharField("链接地址", max_length=64)
    sequence = models.CharField('顺序', max_length=1, choices=SEQ_CHOICES, unique=True)

    def __str__(self):
        return self.text


class ArticleItem(BaseArticle):
    MAX_ITEM = 3
    SEQ_CHOICES = get_sequence_choice(MAX_ITEM)

    title2 = models.CharField('副标题', max_length=64, blank=True, null=True)

    # 显示顺序
    sequence = models.CharField('顺序', max_length=1, choices=SEQ_CHOICES, unique=True)

    # 图标
    cover = models.ForeignKey('Document', help_text='文章的封面图标')
