# -*- coding: utf-8 -*-
import os
import shutil
from sites.settings import MEDIA_ROOT
from apps.core.models import Project, Document

__all__ = [
    'add_document', 'bulk_add_documents', 'create_core_project',
]


def add_document(document, name=""):
    """Add a document

    :param document: document path
    :param name: document name
    :return: True of false
    """
    document_name = os.path.basename(document)
    documents_root = os.path.join(MEDIA_ROOT, Document.get_upload_path())

    if not os.path.isfile(document):
        print("File:{0:s} is not exists!".format(document))
        return True

    try:

        name = name or os.path.splitext(document_name)[0]
        if not Document.objects.filter(name=name).exists():

            if not os.path.isdir(documents_root):
                os.makedirs(documents_root)

            # Copy file to documents root and create documents instance
            shutil.copy(document, os.path.join(documents_root, document_name))
            Document.objects.create(name=name, file=Document.get_upload_path() + "/" + document_name)

    except shutil.Error as e:
        print("Copy file:{0:s} to documents root:{1:s} error:{2:s}".format(document, documents_root, e))
        return False

    return True


def bulk_add_documents(path):
    """Bluk Documents

    :param path: documents path
    :return: Success True
    """
    if not os.path.isdir(path):
        print("Path:{0:s} is not a directory!".format(path))
        return False

    for file_name in os.listdir(path):
        add_document(os.path.join(path, file_name))

    return True


def create_core_project(name, phone, address, cover, ico):
    """Create a core project instance

    :param name: project name
    :param phone: phone number
    :param address: contact address
    :param cover: homepage cover
    :param ico: browser tag ico
    :return:  True of False
    """
    # Project only allow create one instance
    if len(Project.objects.all()) != 0:
        print("Project already has one instance!")
        return False

    # Get Documents instance
    ico_file = Document.objects.filter(name=ico)
    cover_file = Document.objects.filter(name=cover)

    if not ico_file.exists() or not cover_file.exists():
        print("Cover and browser ico can't found!")
        return False

    # Start create project
    Project.objects.create(name=name, phone=phone, address=address, cover=cover_file[0], ico=ico_file[0])
    return True
