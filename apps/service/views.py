# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from ..core.models import Project, NavigationBar
from .models import Service, ServiceItem


def service(request):
    """展示关于页面

    :param request:
    :return:
    """
    site = get_object_or_404(Project)
    services = ServiceItem.objects.all().order_by('sequence')
    navigation_list = NavigationBar.objects.all().order_by('sequence')
    context = {
        'site': site,
        'services': services,
        'location': Service.url,
        'navigation_list': navigation_list,
    }
    return render(request, 'service/service.html', context)
