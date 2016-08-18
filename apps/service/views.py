# -*- coding: utf-8 -*-
from django.shortcuts import render
from ..core.models import NavigationModel
from .models import Service, ServiceItem


def service(request):
    """展示关于页面

    :param request:
    :return:
    """
    context = NavigationModel.get_navigation_context(Service)
    context['services'] = ServiceItem.objects.all().order_by('sequence')

    return render(request, 'service/service.html', context)
