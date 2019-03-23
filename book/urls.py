from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.index, name='index'),
    path('books/<int:book_id>/', views.detail, name='detail'),
    path('books/<int:book_id>/edit/', views.edit, name='edit'),
    path('books/<int:book_id>/delete/', views.delete, name='delete'),
    path('books/new/', views.create, name='new'),
    path('mypage/', views.mypage, name='mypage'),
]