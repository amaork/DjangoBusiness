# -*- coding: utf-8 -*-
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import generic


from .forms import DocumentForm
from .models import *


__all__ = ['file_list', 'IndexView']


def file_list(request):
    # Handle file upload
    if request.mothod == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_vaild():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to document list after post
            return HttpResponseRedirect(reverse('file_list'))
    else:
        form = DocumentForm()

    # Load documents form list page
    documents = Document.objects.all()
    return render(request, 'file_list.html', {"documents": documents, "form": form})


def homepage(request):
    site = get_object_or_404(Project)
    navis = NavigationItem.objects.all()
    headers = HeaderItem.objects.all()
    articles = ArticleItem.objects.all()
    context = {'site': site, 'navis': navis, 'headers': headers, 'articles': articles}
    return render(request, 'homepage/index.html', context)
