from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, FileInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text', 'author', 'tag', 'date', 'image']

        widgets = {
            'title': TextInput(attrs={
                'type': "text", 'placeholder': "Title"
            }),
            'full_text': Textarea(attrs={
                'class': 'title-of-article', 'placeholder': 'Текст статьи'
            }),
            'author': TextInput(attrs={
                'class': 'title-of-article', 'placeholder': 'Автор'
            }),
            'tag': TextInput(attrs={
                'class': 'title-of-article', 'placeholder': 'Тэги'
            }),
            'image': FileInput(attrs={
                'class': "form-control", 'id': "inputGroupFile02"
            })
        }
