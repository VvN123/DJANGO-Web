# Generated by Django 4.1.4 on 2023-06-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='description_short',
            field=models.TextField(blank=True, null=True),
        ),
    ]