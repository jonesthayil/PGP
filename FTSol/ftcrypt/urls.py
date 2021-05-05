from django.urls import path
from ftcrypt import views
from ftcrypt.views import ECRTFILE
from django.conf.urls import url

urlpatterns = [
    url('asdas/', ECRTFILE.as_view(), name='file-upload'),
    path('', views.ecrtfil, name='ecrtfil'),
]
