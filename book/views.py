from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm


def index(request):
    latest_book_list = Book.objects.order_by('updated_at')
    context = {'latest_book_list': latest_book_list}
    return render(request, 'book/index.html', context)


def detail(request, book_id):
    return HttpResponse("detail %s" % book_id)


def edit(request, book_id):
    return HttpResponse("edit %s" % book_id)


def delete(request, book_id):
    return HttpResponse("delete %s" % book_id)


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = "book/create.html"
    success_url = reverse_lazy('book:index')


def mypage(request):
    return HttpResponse("mypage")
