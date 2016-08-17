# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import UserCommentForm
from ..core.models import Project, NavigationBar
from .models import CompanyInfo, ContactInfo, CommentMessage


def about(request):
    """展示关于页面

    :param request:
    :return:
    """
    site = get_object_or_404(Project)
    about_us = get_object_or_404(CompanyInfo)
    navigation_list = NavigationBar.objects.all().order_by('sequence')
    context = {
        'site': site,
        'about_us': about_us,
        'location': CompanyInfo.url,
        'navigation_list': navigation_list,
    }
    return render(request, 'about/about.html', context)


def contact_us(request):
    """展示联系我们页面,保存用户提交的留言信息

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = UserCommentForm(request.POST)
        if form.is_valid():
            # 保存用户留言信息
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            wechat = request.POST.get('wechat')
            comment = request.POST.get('comment')
            CommentMessage.add_user_comment(name, phone, wechat, comment)

            # 发送成功信息到 contact_us 页面
            messages.add_message(request, messages.INFO, '留言成功,我们会尽快联系您!')
            return HttpResponseRedirect('/{0:s}/'.format(ContactInfo.url))
        else:
            # 发送失败信息到 contact_us 页面
            messages.add_message(request, messages.WARNING, '请完整填写留言信息')
    else:
        form = UserCommentForm()

    site = get_object_or_404(Project)
    contact = get_object_or_404(ContactInfo)
    navigation_list = NavigationBar.objects.all().order_by('sequence')
    context = {
        'form': form,
        'site': site,
        'contact': contact,
        'location': ContactInfo.url,
        'navigation_list': navigation_list,
    }
    return render(request, 'about/contact_us.html', context)
