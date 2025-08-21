from django.db import models

from .base_model import BaseModel

class ArtistModel(BaseModel):
    """
    Исполнитель — музыкант, группа или автор.
    """
    name: str = models.CharField(
        max_length=255,
        verbose_name="Имя исполнителя",
        help_text="Полное имя или псевдоним исполнителя"
    )

    class Meta:
        db_table = 'artists'
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='idx_artist_name'),
        ]

    def __str__(self) -> str:
        return self.name

