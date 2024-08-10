from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('add_article', views.add_article),
    path('article-<int:pk>', views.ArticleDetailedView.as_view(), name='Article-detailed'),
    path('article-<int:pk>/update', views.ArticleUpdateView.as_view(), name='Update_article')
]