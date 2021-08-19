from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

menu = [
        {'title': 'Main page', 'url_name': 'home'},
        {'title': "About site", 'url_name': 'about'},
        {'title': "Profile", 'url_name': 'profile'},
        {'title': "Sign up", 'url_name': 'registration'},
        {'title': "Sign in", 'url_name': 'authorization'}
        ]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'pixpeople/index.html/', context=context)


def authorization(request):
    context = {
        'menu': menu,
        'title': 'Авторизация'
    }
    return render(request, 'pixpeople/authorization.html/', context=context)


def registration(request):
    context = {
        'menu': menu,
        'title': 'Регистрация'
    }
    return render(request, 'pixpeople/registration.html/', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
    }
    return render(request, 'pixpeople/about.html/', context=context)


def profile(request):
    context = {
        'menu': menu,
        'title': 'Профиль'
    }
    return render(request, 'pixpeople/profile.html/', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

