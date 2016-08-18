from django.conf.urls import url
from .models import ContactInfo, CompanyInfo
from .views import about, contact_us

app_name = 'about'
urlpatterns = [

    url(r'^{0:s}/$'.format(CompanyInfo.url), about, name='about'),
    url(r'^{0:s}/$'.format(ContactInfo.url), contact_us, name="contact_us"),
]
