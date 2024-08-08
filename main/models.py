from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField('Название',max_length=150)
    content = models.TextField('Содержание')
    creation_datetime = models.DateTimeField('Дата и время создания', default=timezone.now)
    publication_datetime = models.DateTimeField('Дата и время публикации')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"