from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('books/', views.index, name='index'),
    path('books/<int:book_id>/', views.detail, name='detail'),
    path('books/<int:book_id>/edit/', views.edit, name='edit'),
    path('books/<int:book_id>/delete/', views.delete, name='delete'),
    path('books/new/', views.Create.as_view(), name='new'),
    path('mypage/', views.mypage, name='mypage'),
]