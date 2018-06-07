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
        post = Post.objects.create(
            author=request.user,
            title=request.POST['title'],
            text=request.POST['text']
        )

        # return HttpResponse(f'id:{post.id} title:{post.title} text:{post.text}')
        # return render(request, 'blog/post_create.html', context)
        return redirect('post-list')
    else:
        return render(request, 'blog/post_create.html')

def post_delete(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()
    return redirect('post-list')


def post_edit(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.save()
    return render(request,'blog/post_edit')
