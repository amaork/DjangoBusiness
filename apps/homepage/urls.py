from django.conf.urls import url
from ..core.models import Project
from .views import homepage


app_name = 'homepage'
urlpatterns = [

    url(r'^$', homepage, name='index'),
    url(r'^{0:s}/$'.format(Project.url), homepage, name='index'),
]
