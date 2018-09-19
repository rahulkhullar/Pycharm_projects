
from django.conf.urls import url
#from django.contrib import admin
#from django.contrib.auth import views as auth_views

from . import views

app_name = 'oms'

urlpatterns = [
    # ex: /polls/
#    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
#    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
#    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^$', views.index, name = 'index'),
#    url(r'^login/$', auth_views.login, name='login'),
#    url(r'^login/$', auth_views.logout, name='logout'),
    url(r'^(?P<item_id>[0-9]+)/savecust', views.savecust, name='savecust'),
    # url(r'^savecust/', views.savecust, name='savecust'),
    url(r'^shop/(?P<item_id>[0-9]+)/$', views.addcust, name='addcust'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^order/$', views.order, name='order')
#    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
