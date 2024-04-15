# Generated by Django 5.0.4 on 2024-04-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_books_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('mystery', 'Mystery'), ('thriller', 'Thriller'), ('romance', 'Romance'), ('fantasy', 'Fantasy'), ('horror', 'Horror'), ('drama', 'Drama'), ('comedy', 'Comedy'), ('action', 'Action'), ('crime', 'Crime'), ('western', 'Western'), ('autobiography', 'Autobiography')], max_length=13),
        ),
    ]