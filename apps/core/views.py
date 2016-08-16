# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import DocumentForm
from .models import Document


def document_upload(request):
    # Handle file upload
    if request.mothod == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_vaild():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to document list after post
            return HttpResponseRedirect(reverse('document_upload'))
