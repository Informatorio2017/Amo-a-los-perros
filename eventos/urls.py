from django.conf.urls import url

from eventos.views import eventos, nuevo

urlpatterns = [
    url(r'^$', eventos, name='eventos'),
    url(r'^nuevo/$', nuevo, name='nuevo'),
]
