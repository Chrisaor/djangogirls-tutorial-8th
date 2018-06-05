from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        id = request.user
        post = Post.objects.create(author=id, title=title,text=text)

        return HttpResponse(f'id:{post.id} title:{post.title} text:{post.text}')
        # return render(request, 'blog/post_create.html', context)
    else:
        return render(request, 'blog/post_create.html')
