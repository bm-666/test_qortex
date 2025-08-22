from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albummodel',
            options={'ordering': ['-release_year'], 'verbose_name': 'Альбом', 'verbose_name_plural': 'Альбомы'},
        ),
        migrations.RemoveField(
            model_name='albummodel',
            name='title',
        ),
    ]
