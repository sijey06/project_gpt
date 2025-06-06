from django.contrib.auth.models import User
from django.db import models

from .constants import LENGTH_ID


class PromptTemplate(models.Model):
    """
    Хранит различные шаблоны промптов,
    которые пользователи могут выбирать.
    """

    title = models.CharField(max_length=LENGTH_ID, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(
        upload_to='templat/',
        verbose_name='Изображение',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Шаблон'
        verbose_name_plural = 'Шаблоны'


class Application(models.Model):
    """Модель приложения с идентификатором и набором шаблонов."""

    app_id = models.CharField(
        max_length=LENGTH_ID,
        unique=True,
        verbose_name='ID приложения'
    )
    name = models.CharField(
        max_length=LENGTH_ID,
        verbose_name='Имя приложения'
    )
    templates = models.ManyToManyField(
        PromptTemplate,
        verbose_name='Связанные шаблоны'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'


class Statistics(models.Model):
    """Модель статистики для учета связи с приложением."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='statistics',
        verbose_name='Пользователь'
    )
    app = models.ForeignKey(
        Application,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Приложение'
    )
    total_requests = models.PositiveIntegerField(
        default=0, verbose_name='Общее число запросов'
    )
    last_request_time = models.DateTimeField(
        auto_now=True, verbose_name='Время последнего запроса'
    )

    def increment_total_requests(self):
        """Метод для увеличения числа запросов пользователя."""
        self.total_requests += 1
        self.save(update_fields=['total_requests'])

    def __str__(self):
        username_part = f'{self.user.username}/'
        app_name_part = getattr(self.app, 'name', '-')
        requests_count = f' : Запросы({self.total_requests})'
        return username_part + app_name_part + requests_count

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
