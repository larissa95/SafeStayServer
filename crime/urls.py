__author__ = 'larissa'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get', views.get_crimes, name='get_crimes'),
]