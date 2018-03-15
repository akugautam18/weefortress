from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<team_id>[0-9]+)/$', views.team_detail, name='team_detail'),
    url(r'^gm_d/(?P<team_id>[0-9]+)/$', views.team_detail, name='game_detail'),
    url(r'^test/$', views.test, name='test'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^service/$', views.service, name='service'),
]
