from django import forms
from django.forms import ModelForm
from .models import Article
from django.utils import timezone

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'publication_datetime', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class':'title','placeholder':'Введите название'}),
            'publication_datetime':forms.DateTimeInput({'class':'publication_datetime','type': 'datetime-local', 'default':timezone.now()}),
            'content':forms.Textarea({'class':'content','placeholder':'Введите содержание статьи'})
        }
        error_messages = {
            'title':{'required':'Заполните это поле'},
            'publication_datetime':{'required':'Заполните это поле'},
            'content':{'required':'Заполните это поле'},
        }