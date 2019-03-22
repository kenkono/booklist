from django.http import HttpResponse
from django.shortcuts import render

from .models import Book


def index(request):
    return render(request, 'book/index.html')


def detail(request, book_id):
    return HttpResponse("detail %s" % book_id)


def edit(request, book_id):
    return HttpResponse("edit %s" % book_id)


def delete(request, book_id):
    return HttpResponse("delete %s" % book_id)


def create(request):
    return HttpResponse("create")


def mypage(request):
    return HttpResponse("mypage")


def login(request):
    return render(request, 'book/login.html')


def logout(request):
    return HttpResponse("logout")


def signin(request):
    return HttpResponse("siginin")
