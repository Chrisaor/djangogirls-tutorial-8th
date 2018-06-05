from django.conf.urls import url

from .views import post_list, post_detail, post_create

urlpatterns = [
    url(r'^$', post_list, name='post-list'),
    url(r'^(\d+)/', post_detail, name='post-detail'),
    url(r'write/', post_create, name='post-create'),
]