from django.contrib import admin
from apps.book.models import Book, BookMark, RatingComment


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'created_at', 'bookmark_count')
    list_filter = ('title',)


class RatingCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rating', 'comment')
    list_filter = ('rating',)


class BookMarkAdmin(admin.ModelAdmin):
    list_display = ('book', 'user')


admin.site.register(Book, BookAdmin)
admin.site.register(RatingComment, RatingCommentAdmin)
admin.site.register(BookMark, BookMarkAdmin)
