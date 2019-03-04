# Generated by Django 2.1.7 on 2019-02-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190228_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu',
            field=models.CharField(choices=[('about', 'обо мне'), ('group', 'наша группа'), ('docs', 'документы'), ('news', 'новости'), ('contacts', 'контакты')], default='about', max_length=20, verbose_name='корневое меню'),
        ),
    ]