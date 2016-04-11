from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'post/new/$', views.post_new, name='post_new'),
    url(r'post/edit/(?P<post_id>[0-9]+)/$', views.post_new, name='post_edit'),
    url(r'post/manage/$', views.post_manage, name='post_manage'),
    url(r'post/delete/(?P<post_id>[0-9]+)/$', views.post_delete, name='post_delete'),
    url(r'api/posts/(?P<post_offset>[0-9]+)/(?P<number_of_posts>[0-9]+)/$', views.post_get, name='post_get'),
]
