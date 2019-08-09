from django.urls import path
from django.conf.urls import *

from . import views, testdb

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^testdb$', testdb.testdb),
]
