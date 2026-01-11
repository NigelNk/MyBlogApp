from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

CATEGORIES = (
    ('science', 'Science'),
    ('technology', 'Technology'),
    ('health', 'Health'),
    ('politics', 'Politics'),
    ('business', 'Business'),
)


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORIES, default='science')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False)
    content = RichTextField(config_name='default')
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)

    likes = models.ManyToManyField(
        get_user_model(),
        related_name='liked_articles',
        blank=True,
    )

    def __str__(self):
        return self.title

    @property
    def is_edited(self):
        return self.updated_at > self.created_at

    @property
    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.pk})
