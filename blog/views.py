from django.shortcuts import render, get_object_or_404
from .models import Post



# Create your views here.
def post_list(request):#takes the request object as the only parameter.This parameter is required by all views.
    posts = Post.published.all()#retrieve all posts with PUBLISHED status
    return render(request, 'post/list.html', {'posts': posts})#renders request object,template path,context variables in the given template

def post_detail(request, post, year, month, day,):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )#published post with the given slug and publication date
    return render(request,'post/detail.html', {'post': post })  

