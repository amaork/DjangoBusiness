# -*- coding: utf-8 -*-
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import generic


from .forms import DocumentForm
from .models import *


__all__ = ['document_upload', 'IndexView']


def document_upload(request):
    # Handle file upload
    if request.mothod == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_vaild():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to document list after post
            return HttpResponseRedirect(reverse('document_upload'))


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


def about(request):
    site = get_object_or_404(Project)
    navigation_list = NavigationBar.objects.all()
    context = {'site': site, 'navigation_list': navigation_list, 'location': 'about'}
    return render(request, 'homepage/about.html', context)
