# Generated by Django 4.0.4 on 2022-06-09 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messanger', '0004_message_is_important'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='iv',
            field=models.CharField(default='no_key', max_length=255),
        ),
    ]
