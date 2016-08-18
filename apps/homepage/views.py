# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404


from ..core.models import Project, NavigationModel
from .models import HorizontalItem, VerticalItem


def homepage(request):
    context = NavigationModel.get_navigation_context(Project)
    context['vertical_list'] = VerticalItem.objects.all().order_by('sequence')
    context['horizontal_list'] = HorizontalItem.objects.all().order_by('sequence')

    return render(request, 'homepage/index.html', context)
