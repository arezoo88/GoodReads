from django.urls import path, include
from apps.book.api.v1.views import BookViewSet, BookDetailViewSet, RatingCommentViewSet

app_name = 'book.api.v1'


urlpatterns = [
    path('books/', BookViewSet.as_view({'get': 'list'}), name='book-list'),
    path('books/<int:pk>/',
         BookDetailViewSet.as_view({'get': 'retrieve'}), name='book-detail'),
    path('rate-comment/',
         RatingCommentViewSet.as_view({'post': 'create'}), name='rate-and-comment'),

]
