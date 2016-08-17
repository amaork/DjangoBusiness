from django.conf.urls import url
from .views import about, comment

app_name = 'about'
urlpatterns = [

    url(r'^about/$', about, name='about'),
    url(r'^comment', comment, name="comment"),
]
