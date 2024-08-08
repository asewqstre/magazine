from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('add_article', views.add_article)
]