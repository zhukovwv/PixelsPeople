from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

menu = ["About", "Sign up", "Sign in"]


def index(request):
    return render(request, 'pixpeople/index.html/', {'menu': menu, 'tittle': 'Главная страница'})


def authorization(request):
    return render(request, 'pixpeople/authorization.html/', {'menu': menu, 'tittle': 'Авторизация'})


def registration(request):
    return render(request, 'pixpeople/registration.html/', {'menu': menu, 'tittle': 'Регистрация'})


def profile(request, profid):
    return HttpResponse('Тут будет профиль')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

