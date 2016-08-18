# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import Http404
from django.db import models
import string
import os

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
    context_name = ""

    self_define_cover = models.ForeignKey('Document', related_name='self_define', blank=True, null=True,
                                          verbose_name='自定义封面')

    @staticmethod
    def get_top_sequence():
        return 0

    @staticmethod
    def get_bottom_sequence():
        return NavigationBar.MAX_ITEM - 1

    def save(self, *args, **kwargs):
        if len(self.text) and len(self.url) and self.sequence != -1:
            if not NavigationBar.objects.filter(url=self.url, text=self.text):
                NavigationBar.objects.create(text=self.text, url=self.url, sequence=self.sequence)
        super(NavigationModel, self).save(*args, **kwargs)

    @staticmethod
    def get_navigation_context(core_type):
        """
        生成导航需要的必须 context 数据
        :param core_type: 核心数据类型
        :return:
        """

        if not issubclass(core_type, NavigationModel):
            return Http404("Do not found core data")

        # 获取改页面的核心数据
        data = get_object_or_404(core_type)

        # 获取导航必须的公用数据
        site = get_object_or_404(Project)
        navigation_list = NavigationBar.objects.all().order_by('sequence')

        # 如果有自定义封面使用自定义封面,否则使用 Project 默认的封面
        cover = data.self_define_cover or site.cover

        context = {'site': site, 'cover': cover, 'location': data.url, 'navigation_list': navigation_list}

        # 将核心数据打包到 context 中
        if data.context_name:
            context[data.context_name] = data

        return context


class Project(NavigationModel):
    """
    核心 Model 首先需要创建一个 Project Instance，成功保存之后将自动完成一下动作：
    1. 创建 core.CompanyInfo 保存名称信息
    2. 创建 core.ContactInfo 保存电话与地址信息
    3. 创建 主页、关于、联系我们等基本的导航栏(NavigationBar)
    """
    text = "主页"
    url = 'homepage'
    sequence = NavigationModel.get_top_sequence()

    name = models.CharField('名称', max_length=16)
    phone = models.CharField('电话', max_length=64, default='')
    address = models.CharField('地址', max_length=128, default='')
    cover = models.ForeignKey('Document', verbose_name='主页封面', related_name='cover')
    ico = models.ForeignKey('Document', verbose_name='浏览器 ICO', related_name='ico')

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
    PATH_FORMAT = "documents/%Y/%m/%d"

    name = models.CharField(max_length=32, unique=True)
    file = models.FileField(upload_to=PATH_FORMAT)

    def __str__(self):
        return self.name

    def url(self):
        return self.file.url

    def file_path(self):
        return self.file.name

    @staticmethod
    def get_upload_path():
        return timezone.now().strftime(Document.PATH_FORMAT)


class NavigationBar(models.Model):
    """
    导航栏
    """
    MAX_ITEM = 10
    SEQ_CHOICES = get_sequence_choices(MAX_ITEM)

    text = models.CharField("名称", max_length=16)
    url = models.CharField("地址", max_length=64)
    sequence = models.CharField('顺序', max_length=1, choices=SEQ_CHOICES)

    def __str__(self):
        return self.text


@receiver(pre_delete, sender=Document)
def delete_document(sender, instance, **kwargs):
    if not isinstance(instance, Document):
        return

    if instance.file and os.path.isfile(instance.file.path):
        os.remove(instance.file.path)


@receiver(pre_save, sender=Document)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not isinstance(instance, Document):
        return False

    if not instance.pk:
        return False

    try:

        new = instance.file
        old = Document.objects.get(pk=instance.pk).file

        # New file and old file is not sameone
        if (not (old == new)) and os.path.isfile(old.path):
            os.remove(old.path)
    except Document.DoesNotExist:
        return False
