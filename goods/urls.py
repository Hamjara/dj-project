from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^good/(?P<good_id>\w+)/$', views.good, name='good'),
]
