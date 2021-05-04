from django.urls import path
from ftcrypt import views
from django.conf.urls import url
from .views import MyUploadView

urlpatterns = [
    path('', views.ecrtfile, name='ecrtfile'),
    url('asdasd/', MyUploadView.as_view(), name='upload'),
]
