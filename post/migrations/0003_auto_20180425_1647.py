# Generated by Django 2.0.4 on 2018-04-25 20:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_post_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('pub_date', models.DateTimeField()),
                ('body', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]