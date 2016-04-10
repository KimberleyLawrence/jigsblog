from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'post/new/$', views.post_new, name='post_new'),
    url(r'post/edit/(?P<post_id>[0-9]+)/$', views.post_new, name='post_edit'),
]
