# Generated by Django 4.2.5 on 2023-10-21 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Postit', '0008_alter_books_title_alter_posts_subtite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('text', models.CharField(max_length=100, null='null')),
            ],
        ),
    ]
