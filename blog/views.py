from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'title': 'Blog Post One',
        'author': 'John Doe',
        'content': 'This is a blog post',
        'date': '22 August 2020'
    },

    {
        'title': 'Blog Post Two',
        'author': 'Jane Doe',
        'content': 'This is another blog post',
        'date': '23 August 2020'
    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
