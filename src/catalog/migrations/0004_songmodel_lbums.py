from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_albummodel_options_albummodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='songmodel',
            name='lbums',
            field=models.ManyToManyField(related_name='songs', through='catalog.AlbumSongModel', to='catalog.albummodel'),
        ),
    ]
