# Generated by Django 5.0.4 on 2024-04-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_money',
            field=models.FloatField(default=200),
        ),
    ]
