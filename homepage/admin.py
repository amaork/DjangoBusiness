from django.contrib import admin

from .models import *


# Register your models here.
admin.site.register(Project)
admin.site.register(Document)
admin.site.register(HeaderItem)
admin.site.register(ArticleItem)
admin.site.register(NavigationItem)
