# Generated by Django 4.0.4 on 2022-06-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messanger', '0003_rename_rooms_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_important',
            field=models.BooleanField(default=False),
        ),
    ]