from django.views import generic
from .models import Post
from django.shortcuts import render

# Create your views here.

def blog(request):
    """
    renders the blog page page
    """

    return render(request, 'blog/blog.html')