from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {

            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the article title',
                'maxlength': '100',
                'style': 'font-weight: bold; font-size: 18px;'
            }),

            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Short description (Anons)',
                'minlength': '20',
                'style': 'font-size: 14px; color: #555;'
            }),

            "date": DateTimeInput(attrs={'class': 'form-control',
                                         'placeholder': 'Date',
                                         "type" : "date", }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the full content of the article',
                'rows': 10,
                'style': 'font-size: 16px; padding: 10px; color: #333;',
                'spellcheck': 'true'
            }),
        }