from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts=Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})
    #render function renders the list of posts to the given template

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
# the post_detail view (function) takes post details to retrieve a published post
# with the given slug and date.
