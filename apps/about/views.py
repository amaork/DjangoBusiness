# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404

from .models import CompanyInfo
from ..core.models import Project, NavigationBar


def about(request):
    site = get_object_or_404(Project)
    about_us = get_object_or_404(CompanyInfo)
    navigation_list = NavigationBar.objects.all()
    context = {
        'site': site,
        'location': 'about',
        'about_us': about_us,
        'navigation_list': navigation_list,
    }
    return render(request, 'about/about.html', context)
