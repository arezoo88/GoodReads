from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models import Avg, Q

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_('Created_at'),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated_at'),
        auto_now=True
    )

    class Meta:
        abstract = True


class Book(BaseModel):
    title = models.CharField(
        max_length=200,
        verbose_name=_('Title'),
    )
    summary = models.TextField(
        verbose_name=_('Summary')
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return self.title

    @property
    def bookmark_count(self):
        # cach with redis #TODO
        return self.bookmarks.count()

    @property
    def average_rating(self):
        ratings = self.ratings.all()
        return ratings.aggregate(Avg('rating'))['rating__avg'] if ratings else None

    @property
    def rating_count(self):
        return self.ratings.exclude(rating__isnull=True).count()

    def comment_count(self):
        return self.ratings.exclude(Q(comment__isnull=True) | Q(comment="")).count()


class RatingComment(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name=_('Book'),
    )
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)],
        verbose_name=_('Rating'),
        null=True
    )
    comment = models.TextField(
        verbose_name=_('Comment'),
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ('user', 'book')
        ordering = ['-created_at']
        verbose_name = _('RatingComment')
        verbose_name_plural = _('RatingComments')

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


class BookMark(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name=_('Book'),
        related_name='bookmarks'
    )

    class Meta:
        unique_together = ('user', 'book')
        ordering = ['-created_at']
        verbose_name = _('BookMark')
        verbose_name_plural = _('BookMarks')
