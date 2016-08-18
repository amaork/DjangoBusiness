from django.conf.urls import url
from .views import service
from .models import Service

app_name = 'service'
urlpatterns = [

    url(r'^{0:s}/$'.format(Service.url), service, name='{0:s}'.format(Service.url)),
]
