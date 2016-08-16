# -*- coding: utf-8 -*-
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import generic

from .models import AboutUs
from ..homepage.models import Project, NavigationBar


def about(request):
    site = get_object_or_404(Project)
    about_us = get_object_or_404(AboutUs)
    navigation_list = NavigationBar.objects.all()
    context = {
        'site': site,
        'location': 'about',
        'about_us': about_us,
        'navigation_list': navigation_list,
    }
    return render(request, 'about/about.html', context)
