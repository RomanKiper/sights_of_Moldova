from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': "about"},
        {'title': "Добавить статью", 'url_name': "add_page"},
        {'title': "Обратная связь", 'url_name': "contact"},
        # {'title': "Отзывы", 'url_name': "reviews"},
        {'title': "Войти", 'url_name': "login"}
        ]

def index(request):
    posts = Attractions.objects.all()
    context = {
        "posts": posts,
        "menu": menu,
        "title": "Главная страница",
        "cat_selected": 0,
    }
    return render(request, "attractions/index.html", context=context)


def about(request):
    return render(request, "attractions/about.html", {"menu": menu, "title": "О сайте"})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    return render(request, "attractions/addpage.html", {'form': form, 'menu': menu, 'title': "Добавление статьи"})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def reviews(request):
    return HttpResponse("Отзывы")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_post(request, post_slug):
    post = get_object_or_404(Attractions, slug=post_slug)

    context = {
        "post": post,
        "menu": menu,
        "title": post.name,
        "cat_selected": post.cat_id,
    }

    return render(request, "attractions/post.html", context=context)

def show_category(request, cat_id):
    posts = Attractions.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404

    context = {
        "posts": posts,
        "menu": menu,
        "title": "Отображение по рубрикам",
        "cat_selected": cat_id,
    }
    return render(request, "attractions/index.html", context=context)
