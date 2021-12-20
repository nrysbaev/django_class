from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='books_view'),
    path('books/<int:id>/', views.BookDetailView.as_view(), name='book_detail_view'),
    path('books/<int:id>/update', views.BookUpdateView.as_view(), name='book_update_view'),
    path('books/<int:id>/delete', views.BookDeleteView.as_view(), name='book_delete_view'),
    path('book-create/', views.BookCreateView.as_view(), name='book_create_view'),
    path('comment-create/<int:id>/', views.comment_create, name='comment_create_view'),

]
