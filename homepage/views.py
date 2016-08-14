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
    navis = NavigationItem.objects.all()
    headers = HeaderItem.objects.all()
    articles = ArticleItem.objects.all()
    context = {
        'site': site,
        'navis': navis,
        'headers': headers,
        'articles': articles,
        'location': 'homepage'}
    return render(request, 'homepage/index.html', context)


def about(request):
    site = get_object_or_404(Project)
    navis = NavigationItem.objects.all()
    context = {'site': site, 'navis': navis, 'location': 'about'}
    return render(request, 'homepage/about.html', context)
