from django.db import models
from .base_model import BaseModel
from .artist_model import ArtistModel


class AlbumModel(BaseModel):
    """
    Музыкальный альбом, связанный с исполнителем.
    """
    title = models.CharField(
        max_length=255,
        verbose_name="Название альбома",
        help_text="Название альбома"
    )

    artist = models.ForeignKey(
        ArtistModel,
        related_name="albums",
        on_delete=models.CASCADE,
        verbose_name="Исполнитель",
        help_text="Исполнитель, выпустивший альбом"
    )

    release_year = models.PositiveIntegerField(
        verbose_name="Год выпуска",
        help_text="Четырёхзначный год выпуска альбома"
    )

    class Meta:
        db_table = "albums"
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ["-release_year", "title"]
        indexes = [
            models.Index(fields=["artist"], name="idx_album_artist"),
            models.Index(fields=["release_year"], name="idx_album_release_year"),
        ]

    def __str__(self) -> str:
        return f"{self.title} ({self.release_year})"

