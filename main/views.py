from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

class ArticleDetailedView(DetailView):
    model = Article
    template_name = 'main/detailed_view.html'
    context_object_name = 'article'

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'main/edit_article.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'main/delete_article.html'
    success_url = reverse_lazy('main_page')