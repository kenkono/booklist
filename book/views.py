from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Book, Impression
from .forms import BookForm, ImageForm


def index(request):
    latest_book_list = Book.objects.order_by('updated_at')
    context = {'latest_book_list': latest_book_list,
               'form': ImageForm(),
               }
    if request.method == 'GET':
        return render(request, 'book/index.html', context)
    elif request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, initial={'book_id': request.book.id})
        if not form.is_valid():
            raise ValueError('invalid form')

        impression = Impression()
        impression.image = form.cleaned_data['image']
        impression.save()

        return redirect('/books/')


class BookDetail(DetailView):
    model = Book, Impression
    template_name = "book/detail.html"


class BookEdit(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "book/edit.html"
    success_url = reverse_lazy('book:index')


class BookDelete(DeleteView):
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
