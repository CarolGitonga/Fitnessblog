from django.urls import path
from . import views

app_name = 'blog'#allows to organize URLs by application and use the name when referring to them

urlpatterns = [
    path('', views.post_list, name='post_list'),

    #use the publication date and slug for the post detail URL
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail')
]