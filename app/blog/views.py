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
        # 글을 수정하기
        # 1. 수정할 내용 title, text를 가져옴
        # 2. 수정할 Post 인스턴스를 명시

        title = request.POST['title']
        text = request.POST['text']
        post = Post.objects.get(id=post_id)

        # 3. 해당하는 Post인스턴스의 title, text를 수정해서 DB에 저장
        post.title = title
        post.text = text
        post.save()
        # 4. post_detail로 이동
        return redirect('post-detail', post_id)
    else:
        obj = Post.objects.get(id=post_id)
        ctx = {
            'post':obj,
        }
        return render(request,'blog/post_edit.html',ctx)
