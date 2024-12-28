from django.db import models
from django.contrib.auth import get_user_model
from pages.models import Publichinfo


class Location(Publichinfo):

    name = models.CharField(max_length=256, verbose_name="Название места")

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"


class Category(Publichinfo):

    title = models.CharField(max_length=256, verbose_name="Заголовок")

    description = models.TextField(verbose_name="Описание")

    slug = models.SlugField(
        unique=True,
        verbose_name="Идентификатор",
        help_text="Идентификатор страницы для URL; разрешены символы "
        "латиницы, цифры, дефис и подчёркивание.",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"


class Post(Publichinfo):

    title = models.CharField(max_length=256, verbose_name="Заголовок")

    text = models.TextField(verbose_name="Текст")

    pub_date = models.DateTimeField(
        verbose_name="Дата и время публикации",
        help_text="Если установить дату и время в будущем — можно делать "
        "отложенные публикации.",
    )

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="Автор публикации"
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Местоположение",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория"
    )

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"
