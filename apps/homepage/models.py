# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from ..core.models import get_sequence_choices, Document


__all__ = ['HorizontalItem', 'VerticalItem']


class BasicItem(models.Model):
    title = models.CharField('标题', max_length=64)
    abstract = models.TextField('摘要', max_length=1024)

    def __str__(self):
        return self.title


class VerticalItem(BasicItem):
    MAX_ITEM = 3
    SEQ_CHOICES = get_sequence_choices(MAX_ITEM)

    title2 = models.CharField('副标题', max_length=64, blank=True, null=True)
    sequence = models.CharField('顺序', max_length=1, choices=SEQ_CHOICES)
    cover = models.ForeignKey(Document, verbose_name='封面图标')


class HorizontalItem(BasicItem):
    """
    主页横向排列的条目
    """
    MAX_ITEM = 3
    SEQ_CHOICES = get_sequence_choices(MAX_ITEM)

    context = models.TextField('正文', help_text='文章的正文内容')
    sequence = models.CharField('顺序', max_length=1, choices=SEQ_CHOICES)
    cover = models.ForeignKey(Document, verbose_name='文章的封面图标')
