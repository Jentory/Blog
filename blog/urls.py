from django.urls import path, re_path

from . import views

app_name = 'blog'

urlpatterns = [
    path('index', views.index),
    # re_path(r'^article/(?P<article_id>[0-9]+)$', views.article_page),
    path('article/<article_id>', views.article_page, name='article_page'),
    path('edit/<article_id>', views.edit_page, name='edit_page'),
    path('edit/action', views.edit_action, name='edit_action'),
]