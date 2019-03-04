# Generated by Django 2.1.7 on 2019-03-03 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='имя комментатора'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Comment', verbose_name='ответ на комментарий'),
        ),
        migrations.AlterField(
            model_name='news',
            name='fix',
            field=models.BooleanField(blank=True, default=False, verbose_name='закрепить новость как основную'),
        ),
    ]
