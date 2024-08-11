from django.urls import path, include
from apps.book.api.v1.views import BookViewSet

app_name = 'book.api.v1'


urlpatterns = [
    path('books/', BookViewSet.as_view({'get': 'list'}), name='book'),

]
