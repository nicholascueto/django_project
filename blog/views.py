from django.shortcuts import render

posts = [
    {
        'author': 'Nicholas Cueto',
        'title': 'Blog Post',
        'content': 'This is a blog post.',
        'date': 'May 11, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'This is another blog post.',
        'date': 'August 23, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
