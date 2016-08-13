from django.conf.urls import url
from .views import file_list, homepage

app_name = 'homepage'
urlpatterns = [

    url(r'^list/$', file_list, name="file_list"),
    url(r'^$', homepage, name='index'),
]
