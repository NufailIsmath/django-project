from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
  path('', views.BookList.as_view(), name='books_list'),
  path('new', views.BookCreate.as_view(), name='books_new'),
  path('edit/<int:pk>', views.BookUpdate.as_view(), name='books_edit'),
  path('delete/<int:pk>', views.BookDelete.as_view(), name='books_delete'),
]