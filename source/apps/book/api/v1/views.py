from rest_framework.viewsets import ModelViewSet
from apps.book.api.v1.serializers import BookSerializer
from apps.book.models import Book
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer


class BookDetailViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def get_object(self):
        book_obj = get_object_or_404(Book, pk=self.kwargs['pk'])
        return book_obj
