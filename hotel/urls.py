__author__ = 'larissa'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get/(?P<check_in>.+|)/(?P<check_out>.+|)', views.get_hotels, name='get_hotels'),
]