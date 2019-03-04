# Generated by Django 2.1.7 on 2019-03-03 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190303_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.News', verbose_name='комментируемая новость'),
            preserve_default=False,
        ),
    ]