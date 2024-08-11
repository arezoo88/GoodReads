from rest_framework.viewsets import ModelViewSet
from apps.book.api.v1.serializers import BookSerializer
from apps.book.models import Book
from rest_framework.permissions import IsAuthenticated


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
