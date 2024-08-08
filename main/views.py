from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def main(request):
    articles = Article.objects.order_by('-publication_datetime')
    return render(request, 'main/main.html', {'articles':articles})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('/add_article')  # Redirect to a success page or another view
    else:
        form = ArticleForm()

    form = ArticleForm()
    return render(request, 'main/add_article.html', {'form':form})