from django.db import models

class BaseModel(models.Model):
    """
    Абстрактная базовая модель метками времени и общими методами.
    """


    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создано"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Обновлено"
    )

    objects = models.Manager()

    class Meta:
        abstract = True
