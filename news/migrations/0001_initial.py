# Generated by Django 2.1.7 on 2019-03-03 04:50

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя комментатора')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('message', ckeditor.fields.RichTextField(verbose_name='текст комментария')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='время добавления')),
                ('allowed', models.BooleanField(default=False, verbose_name='разрешение на публикацию')),
                ('reply', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='news.Comment', verbose_name='ответ на комментарий')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='заголовок')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='время добавления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='последнее обновление')),
                ('photo', models.ImageField(blank=True, upload_to='news/', verbose_name='фотография')),
                ('fix', models.BooleanField(default=False, verbose_name='закрепить новость как основную')),
                ('text', ckeditor.fields.RichTextField(verbose_name='текст новости')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
                'db_table': 'news',
            },
        ),
    ]