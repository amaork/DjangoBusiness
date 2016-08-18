# -*- coding: utf-8 -*-
from django.db import models
from ..core.models import NavigationModel, Document, get_sequence_choices


class ServiceItem(models.Model):
    MAX_ITEM = 9
    SEQ_CHOICES = get_sequence_choices(MAX_ITEM)

    name = models.CharField('名称', max_length=32, unique=True)
    price = models.IntegerField('价格', default=0)
    desc = models.TextField('描述', max_length=256)
    detail = models.TextField('详情', max_length=1024)
    sequence = models.CharField('顺序', max_length=1, choices=SEQ_CHOICES)
    ico = models.ForeignKey(Document, help_text='图标', blank=True, null=True)

    def save(self, *args, **kwargs):
        if len(Service.objects.all()) == 0:
            Service.objects.create()
        super(ServiceItem, self).save(*args, **kwargs)


class Service(NavigationModel):
    url = 'service'
    text = '服务'
    sequence = NavigationModel.auto_sequence()
    slogan = models.CharField('服务宗旨', max_length=64, blank=True, null=True, default="")
