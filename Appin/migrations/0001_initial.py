# Generated by Django 5.0.6 on 2024-07-12 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('deteil', models.TextField()),
                ('image', models.ImageField(upload_to='about-me/')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('deteil', models.TextField()),
                ('image', models.ImageField(upload_to='article-blog/')),
            ],
        ),
        migrations.CreateModel(
            name='Blog_adventure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('deteil', models.TextField()),
                ('image_for_adbenture', models.ImageField(upload_to='adventure-blog/')),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('deteil', models.TextField()),
                ('image', models.ImageField(upload_to='hobby/')),
            ],
        ),
        migrations.CreateModel(
            name='Name_for_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('name_for_title', models.CharField(max_length=30)),
                ('deteil_title', models.TextField()),
            ],
        ),
    ]
