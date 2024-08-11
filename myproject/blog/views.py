from django.shortcuts import render

# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog_home.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog_detail.html', {'post': post})
