# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404


from ..core.models import Project, NavigationBar
from .models import HorizontalItem, VerticalItem


def homepage(request):
    site = get_object_or_404(Project)
    vertical_list = VerticalItem.objects.all().order_by('sequence')
    horizontal_list = HorizontalItem.objects.all().order_by('sequence')
    navigation_list = NavigationBar.objects.all().order_by('sequence')
    context = {
        'site': site,
        'location': 'homepage',
        'vertical_list': vertical_list,
        'navigation_list': navigation_list,
        'horizontal_list': horizontal_list,
    }

    return render(request, 'homepage/index.html', context)
