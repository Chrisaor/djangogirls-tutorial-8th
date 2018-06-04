from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def post_list(request):
    return render(request, 'blog/post_list.html')