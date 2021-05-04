from django.urls import path
from ftcrypt.views import ECRTFILE
from django.conf.urls import url

urlpatterns = [
    url('', ECRTFILE.as_view(), name='file-upload'),
]
