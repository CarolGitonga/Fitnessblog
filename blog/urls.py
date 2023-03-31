from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'#allows to organize URLs by application and use the name when referring to them

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #path('', views.PostListView.as_view(), name='post_list'),

    #use the publication date and slug for the post detail URL
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),

    path('<int:post_id>/share/', views.post_share, name='post_share'),

    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),

    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

    path('feed/', LatestPostsFeed(), name='post_feed'),
]