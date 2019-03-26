from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.index, name='index'),
    path('list/<int:book_id>/detail/', views.detail, name='detail'),
    path('list/<int:book_id>/edit/', views.edit, name='edit'),
    path('list/<int:book_id>/delete/', views.delete, name='delete'),
    path('list/create/', views.create, name='create'),
    path('list/mypage/', views.mypage, name='mypage'),
    path('list/login/', views.login, name='login'),
    path('list/logout/', views.logout, name='logout'),
    path('list/signin/', views.signin, name='signin'),
]