from django.db import models

from .album_model import AlbumModel
from .base_model import BaseModel
from .song_model import SongModel


class AlbumSongModel(BaseModel):
    """
    Связь между альбомом и песней с указанием позиции (трека) в альбоме.
    """
    album = models.ForeignKey(
        AlbumModel,
        on_delete=models.CASCADE,
        related_name="album_songs",
        verbose_name="Альбом",
        help_text="Альбом, в который входит песня"
    )

    song = models.ForeignKey(
        SongModel,
        on_delete=models.CASCADE,
        related_name="song_albums",
        verbose_name="Песня",
        help_text="Песня, включённая в альбом"
    )

    track_number = models.PositiveIntegerField(
        verbose_name="Номер трека",
        help_text="Порядковый номер песни в альбоме"
    )

    class Meta:
        db_table = "album_songs"
        verbose_name = "Трек в альбоме"
        verbose_name_plural = "Треки в альбомах"
        ordering = ["album", "track_number"]
        constraints = [
            models.UniqueConstraint(
                fields=["album", "track_number"],
                name="unique_album_track_number"
            ),
            models.UniqueConstraint(
                fields=["album", "song"],
                name="unique_album_song"
            ),
        ]
        indexes = [
            models.Index(fields=["album", "track_number"], name="idx_album_track"),
        ]

    def __str__(self) -> str:
        return f"{self.album} - {self.song}"