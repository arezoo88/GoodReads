from rest_framework import serializers
from apps.book.models import Book, RatingComment, BookMark
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.db.models import Count, Avg
from django.db import connection


class BookDetailSerializer(serializers.ModelSerializer):
    rating_distribution = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'summary',
            'comment_count',
            'rating_count',
            'average_rating',
            'rating_distribution',
            'comments'
        ]

    def get_rating_distribution(self, obj):
        ### raw query
        ###با توجه به اینکه به ابجکت دسترسی داشتم از طریق ای دی مربوطه داخل مدل ریتینگ کامنت کوئری زدم و فیلد ریتنگ و تعداد ریتینگ مربوط بهش رو پیدا کردم و از طریق گروپ بای فقط این دو فیلد رو برگردوندم .
        params = []
        query = "SELECT rating,Count(rating) as count FROM book_ratingcomment"
        query += " WHERE book_id = %s  GROUP BY rating"
        params.append(obj.id)

        with connection.cursor() as cursor:
            cursor.execute(query, params)
            distribution = {i: 0 for i in range(1, 6)}
            for entry in cursor.fetchall():
                distribution[entry[0]] = entry[1]
            return distribution

        # # rating_dist = obj.ratings.values(
        # #     'rating').annotate(count=Count('rating'))
        #     distribution = {i: 0 for i in range(1, 6)}
        #     for entry in rating_dist:
        #         distribution[entry['rating']] = entry['count']
            # return distribution

    def get_comments(self, obj):
        ratings = obj.ratings.all()
        return RatingCommentSerializer(ratings, many=True).data


class BookListSerializer(serializers.ModelSerializer):
    is_bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('pk', 'title', 'bookmark_count', 'is_bookmarked')

    def get_is_bookmarked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return BookMark.objects.filter(user=user, book=obj).exists()
        return False


class RatingCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingComment
        fields = ('user', 'book', 'comment', 'rating')
        read_only_fields = ('user',)

    def create(self, validated_data):
        request = self.context.get("request")
        # Remove the book from the user's bookmarks if they rating or comment
        BookMark.objects.filter(
            user=request.user, book=request.data.get('book')).delete()
        book_obj = get_object_or_404(Book, pk=request.data.get('book'))
        obj, created = RatingComment.objects.update_or_create(
            book=book_obj,
            user=request.user,
            defaults={"comment": request.data.get('comment'),
                      "rating": request.data.get('rating'), },
        )
        return obj


class BookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMark
        fields = ('user', 'book')
        read_only_fields = ('user',)
