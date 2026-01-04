from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    image = models.ImageField(upload_to='articles')