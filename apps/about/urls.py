from django.conf.urls import url
from .views import about

app_name = 'about'
urlpatterns = [

    url(r'^about/$', about, name='about'),
]
