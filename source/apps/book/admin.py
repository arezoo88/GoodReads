from django.contrib import admin
from apps.book.models import Book, BookMark


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary','created_at')
    list_filter = ('title',)


class BookMarkAdmin(admin.ModelAdmin):
    list_display = ('book', 'user')


admin.site.register(Book, BookAdmin)
admin.site.register(BookMark, BookMarkAdmin)
