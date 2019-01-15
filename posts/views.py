import datetime

from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post


def home(request):
    # 1) Obtener los 10 últimos posts de la base de datos publicados
    # ordenados de más reciente a más antiguo
    last_posts_published = Post.objects.select_related('author').exclude(pub_date__year__lt=datetime.datetime.now().year).filter(
        status=Post.PUBLISHED).order_by('-last_modification')
    posts_list = last_posts_published[:10]
    # 2) Pasar los posts a la plantilla
    context = {'posts': posts_list}
    return render(request, 'posts/home.html', context)


def post_detail(request, post_pk):
    # 1)Recupero el post indicado desde el modelo
    try:

        post = Post.objects.select_related('author').get(pk=post_pk)
    except Post.DoesNotExist:
        return HttpResponse('Post not found', status=404)

    # 1)Creamos el contexto para el post y lo pasamos a la plantilla
    context = {'post': post}
    return render(request, 'posts/post_detail.html', context)
