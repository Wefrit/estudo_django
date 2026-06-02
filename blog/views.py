from django.shortcuts import render
from blog.data import posts
from django.http import HttpRequest, Http404

def blog (request):
    context = {
        'text': 'Olá Blog',
        'posts': posts,
    }
    return render(request,
                'blog/index.html',
                context,
    )
def post (request:HttpRequest, post_id):
    found_post = None
    title = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            title = post['title']
            break

    if found_post is None:
        raise Http404('Post Not Found')

    context = {
        # 'text': 'Olá Blog',
        'post': found_post,
        'title': title
    }

    return render(request,
                'blog/post.html',
                context,
    )

def exemplo(request):
    context={
            'text':'Olá exemplo',
            }
    return render(request,
                'blog/exemplo.html',
                context,
    )
