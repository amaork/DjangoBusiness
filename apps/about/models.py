# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from ..core.models import Project, Document, NavigationModel


__all__ = ['CompanyInfo', 'ContactInfo', 'CommentMessage']


class CompanyInfo(NavigationModel):
    """
    公司信息
    """
    url = 'about'
    text = "关于"
    context_name = 'about_us'
    sequence = NavigationModel.get_bottom_sequence()

    name = models.CharField('公司名称', max_length=32)
    desc = models.TextField('公司简介', max_length=512)
    value = models.TextField('价值理念', max_length=512)
    comment = models.TextField('用户评价', max_length=512)
    logo = models.ForeignKey(Document, verbose_name='公司 LOGO', related_name='comp_logo', blank=True, null=True)


class ContactInfo(NavigationModel):
    """
    联系我们信息
    """
    url = "contact_us"
    text = '联系我们'
    context_name = 'contact'
    sequence = NavigationModel.get_bottom_sequence() - 1

    name = models.CharField('名称', max_length=32)
    phone = models.CharField('电话', max_length=64, default='')
    email = models.EmailField('邮箱', default='')
    qq = models.CharField('QQ', max_length=16)
    weibo = models.CharField('微薄', max_length=32, default='')
    wechat = models.CharField('微信', max_length=16,  default='')
    address = models.CharField('地址', max_length=128, default='')
    qr_code = models.ForeignKey(Document, verbose_name='微信二维码', related_name='wechat', blank=True, null=True)

    def save(self, *args, **kwargs):
        if len(Project.objects.all()):
            Project.objects.update(phone=self.phone, address=self.address)
        super(ContactInfo, self).save(*args, **kwargs)


class CommentMessage(models.Model):
    """
    用户留言和管理员
    """
    SENDER_CHOICES = (
        ('U', '用户'),
        ('A', '管理员'),
    )

    name = models.CharField('昵称', max_length=32)
    work = models.CharField('工作', max_length=32, default='', blank=True, null=True)
    phone = models.CharField('电话', max_length=11, default='', blank=True, null=True)
    wechat = models.CharField('微信', max_length=16, default='', blank=True, null=True)
    address = models.CharField('地址', max_length=64, default='', blank=True, null=True)
    comment = models.TextField('留言', max_length=128, default="")
    sender = models.CharField('类型', max_length=1, choices=SENDER_CHOICES, default='A')
    avatar = models.ForeignKey(Document, verbose_name="头像", related_name='avatar', blank=True, null=True)

    @staticmethod
    def add_user_comment(name, phone, wechat, comment):
        CommentMessage.objects.create(name=name, phone=phone, wechat=wechat, comment=comment, sender='U')
