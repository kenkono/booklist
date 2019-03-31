from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Book, Impression
from .forms import BookForm


def index(request):
    latest_book_list = Book.objects.order_by('updated_at')
    context = {'latest_book_list': latest_book_list}
    return render(request, 'book/index.html', context)


class BookDetail(DetailView):
    model = Book, Impression
    template_name = "book/detail.html"


def edit(request, book_id):
    return HttpResponse("edit %s" % book_id)


class BookDelete(DetailView):
    model = Book
    success_url = reverse_lazy('book:index')


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = "book/create.html"
    success_url = reverse_lazy('book:index')

    def get_success_url(self):
        raise Exception
        return reverse_lazy('book:index')


def mypage(request):
    return HttpResponse("mypage")
