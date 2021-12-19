from blog.models import Blog
from django.shortcuts import render, get_object_or_404


# Create your views here.

def all_blog(request):
    blog_count = Blog.objects.count()
    blogs = Blog.objects.order_by('-date')
    context = {'blogs': blogs}
    return render(request, 'blog/all_blogs.html', context )


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/detail.html', context)
