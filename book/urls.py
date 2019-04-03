from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('books/', views.index, name='index'),
    path('books/<int:book_id>/', views.BookDetail.as_view(), name='detail'),
    path('books/<pk>/edit/', views.BookEdit.as_view(), name='edit'),
    path('books/<pk>/delete/', views.BookDelete.as_view(), name='delete'),
    path('books/new/', views.BookCreate.as_view(), name='new'),
    path('mypage/', views.mypage, name='mypage'),
]