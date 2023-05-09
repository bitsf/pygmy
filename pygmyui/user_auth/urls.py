from django.urls import re_path as url
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
]