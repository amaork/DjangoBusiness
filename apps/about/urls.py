from django.conf.urls import url
from .views import about, contact_us

app_name = 'about'
urlpatterns = [

    url(r'^about/$', about, name='about'),
    url(r'^contact_us/$', contact_us, name="contact_us"),
]
