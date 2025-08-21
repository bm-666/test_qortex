from django.db import models

from catalog.models.album_model import AlbumModel
from .base_model import BaseModel

class SongModel(BaseModel):
    title: str = models.CharField(
        max_length=255,
        verbose_name="Название песни",
        help_text="Название музыкальной композиции"
    )
    albums = models.ManyToManyField(
        AlbumModel,
        through='AlbumSongModel',
        related_name='songs'
    )

    class Meta:
        db_table = "songs"
        verbose_name = "Песня"
        verbose_name_plural = "Песни"
        ordering = ["title"]
        indexes = [
            models.Index(fields=["title"], name="idx_song_title"),
        ]

    def __str__(self) -> str:
        return self.title