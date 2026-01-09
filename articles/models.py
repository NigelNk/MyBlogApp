from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth import get_user_model

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
    content = RichTextField(config_name='default')
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def is_edited(self):
        return self.updated_at > self.created_at