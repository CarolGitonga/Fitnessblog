from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger

# Create your views here.
def post_list(request):#takes the request object as the only parameter.This parameter is required by all views.
    post_list = Post.published.all()#retrieve all posts with PUBLISHED status
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    
    
    return render(request, 'post/list.html', {'posts': posts})#renders request object,template path,context variables in the given template

def post_detail(request, post, year, month, day,):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )#published post with the given slug and publication date
    return render(request,'post/detail.html', {'post': post })  

