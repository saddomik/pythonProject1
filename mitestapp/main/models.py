from django.db import models


class News(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    anons = models.CharField('Анонс', max_length=150)
    text = models.TextField('Описание')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title
