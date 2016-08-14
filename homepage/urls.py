from django.conf.urls import url
from .views import homepage, about

app_name = 'homepage'
urlpatterns = [

    url(r'^$', homepage, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^homepage/$', homepage, name='index'),
]
