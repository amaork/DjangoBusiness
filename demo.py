# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sites.settings")
django.setup()
import helper


if __name__ == "__main__":
    print("Bulk adding documents....")
    print(helper.bulk_add_documents('images'))

    print("Create core project....")
    print(helper.create_core_project("XXX有限公司", "150xxxxxxxx", "北京", "cover", "logo"))

