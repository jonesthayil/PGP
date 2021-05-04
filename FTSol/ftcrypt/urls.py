from django.urls import path
from ftcrypt import views
from django.conf.urls import url
from .views import ECRTFILE

urlpatterns = [
    url('', ECRTFILE.as_view(), name='file-upload'),
]
