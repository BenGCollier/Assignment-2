# Generated by Django 5.0.9 on 2024-09-14 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_trigram_ext'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]