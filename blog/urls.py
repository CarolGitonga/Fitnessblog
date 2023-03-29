from django.urls import path
from . import views

app_name = 'blog'#allows to organize URLs by application and use the name when referring to them

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),

    #use the publication date and slug for the post detail URL
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),

    path('<int:post_id>/share/', views.post_share, name='post_share')
]