from django.contrib import admin
from django.urls import path
from webapp.views import (
    index_view,
    book_view,
    book_create_view,
    book_update_view,
    book_delete_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='book-list'),
    path('book/<int:pk>/', book_view, name='book-view'),
    path('book/add/', book_create_view, name='book-add'),
    path('book/update/<int:pk>/', book_update_view, name='book-update'),
    path('book/delete/<int:pk>/', book_delete_view, name='book-delete')
]