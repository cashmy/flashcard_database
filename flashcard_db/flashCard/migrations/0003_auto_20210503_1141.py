# Generated by Django 3.1.7 on 2021-05-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashCard', '0002_flashcard_fccollection_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='face',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
