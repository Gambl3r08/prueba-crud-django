# Generated by Django 3.2.4 on 2021-06-23 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancion',
            old_name='fechaLanzamiento',
            new_name='fecha',
        ),
    ]
