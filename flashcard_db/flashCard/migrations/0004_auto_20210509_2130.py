# Generated by Django 3.1.7 on 2021-05-10 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashCard', '0003_auto_20210503_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flashcard',
            old_name='fcCollection_id',
            new_name='fcCollection',
        ),
    ]