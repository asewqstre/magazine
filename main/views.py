from django.shortcuts import render
from .models import Article

def main(request):
    articles = Article.objects.all()
    return render(request, 'main/main.html', {'articles':articles})