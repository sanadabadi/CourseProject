from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('rent/', views.rent_book, name='rent_book'),
    path('return/', views.return_book, name='return_book'),
    path('rentals/', views.rental_list, name='rental_list'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('book/<int:book_id>/update/', views.update_book, name='update_book'),
]
