from django.urls import path
from ftcrypt import views

urlpatterns = [
    path('', views.ecrtfil, name='ecrtfil'),
]
