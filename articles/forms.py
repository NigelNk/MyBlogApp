import bleach
from django import forms
from .models import Article

ALLOWED_TAGS = [
    'a', 'p', 'br', 'strong', 'em',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6'
]

ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title', 'target']
}

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Article title'
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
            strip=True
        )
