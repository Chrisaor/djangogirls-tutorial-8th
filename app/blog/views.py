from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-id')
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

        # return HttpResponse(f'id:{post.id} title:{post.title} text:{post.text}')
        # return render(request, 'blog/post_create.html', context)
        return redirect('post-list')
    else:
        return render(request, 'blog/post_create.html')
