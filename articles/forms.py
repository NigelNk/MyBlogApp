import bleach
from django import forms
from .models import Article

ALLOWED_TAGS = [
    'a', 'p', 'br',
    'strong', 'b', 'em', 'i', 'u',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'ul', 'ol', 'li',
    'blockquote',
    'span',
    'img',
]

ALLOWED_ATTRIBUTES = {
    '*': ['style'],
    'a': ['href', 'title', 'target'],
    'img': ['src', 'alt'],
}

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'content', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Article title'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

    def clean_content(self):
        content = self.cleaned_data['content']
        return bleach.clean(
            content,
            tags=ALLOWED_TAGS,
            attributes=ALLOWED_ATTRIBUTES,
            strip=False
        )
