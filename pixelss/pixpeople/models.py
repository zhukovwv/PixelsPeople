from django.db import models

# Create your models here.


class People(models.Model):
    content = models.TextField(blank=True, verbose_name="Сообщение")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время отправки")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Последние изменение")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чат'
        ordering = ['time_create', 'content']
