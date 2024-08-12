from rest_framework.viewsets import ModelViewSet
from apps.book.api.v1.serializers import BookListSerializer, BookDetailSerializer, RatingCommentSerializer, BookMarkSerializer
from apps.book.models import Book, RatingComment, BookMark
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BookListSerializer


class BookDetailViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BookDetailSerializer

    def get_object(self):
        book_obj = get_object_or_404(Book, pk=self.kwargs['pk'])
        return book_obj


class RatingCommentViewSet(ModelViewSet):
    queryset = RatingComment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RatingCommentSerializer


class BookMarkViewSet(ModelViewSet):
    queryset = BookMark.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BookMarkSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not BookMark.objects.filter(user=request.user, book__pk=request.data.get('book')).exists():
            if not RatingComment.objects.filter(user=request.user, book__pk=request.data.get('book')).exists():
                serializer.save(user=request.user)
                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'error': 'You already commented or rated for this book.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You already bookmarked this book.'}, status=status.HTTP_400_BAD_REQUEST)
