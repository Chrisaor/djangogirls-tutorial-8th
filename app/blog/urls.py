from django.conf.urls import url

from .views import post_list, post_detail, post_create, post_delete, post_edit

urlpatterns = [
    url(r'^$', post_list, name='post-list'),
    url(r'^(\d+)/$', post_detail, name='post-detail'),
    url(r'^(\d+)/delete/$', post_delete, name='post-delete'),
    url(r'^(\d+)/edit/$', post_edit, name='post-edit'),
    url(r'write/$', post_create, name='post-create'),

]