from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def post_list(request):
    html = render_to_string('blog/post_list.html')
    return HttpResponse(html)