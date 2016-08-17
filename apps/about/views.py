# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import UserCommentForm
from .models import CompanyInfo, ContactInfo
from ..core.models import Project, NavigationBar


def about(request):
    form = UserCommentForm()
    site = get_object_or_404(Project)
    contact = get_object_or_404(ContactInfo)
    about_us = get_object_or_404(CompanyInfo)
    navigation_list = NavigationBar.objects.all().order_by('sequence')
    context = {
        'form': form,
        'site': site,
        'location': 'about',
        'contact': contact,
        'about_us': about_us,
        'navigation_list': navigation_list,
    }
    return render(request, 'about/about.html', context)


def comment(request):
    if request.method == 'POST':
        form = UserCommentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/about/')
    else:
        form = UserCommentForm()

    site = get_object_or_404(Project)
    contact = get_object_or_404(ContactInfo)
    about_us = get_object_or_404(CompanyInfo)
    navigation_list = NavigationBar.objects.all().order_by('sequence')
    context = {
        'form': form,
        'site': site,
        'location': 'about',
        'contact': contact,
        'about_us': about_us,
        'navigation_list': navigation_list,
    }
    return render(request, 'about/about.html', context)
