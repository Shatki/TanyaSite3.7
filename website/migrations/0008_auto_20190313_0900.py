# Generated by Django 2.1.7 on 2019-03-13 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20190313_0900'),
        ('website', '0007_auto_20190312_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='menu',
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'страница меню', 'verbose_name_plural': 'страницы меню'},
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu',
            field=models.CharField(choices=[('about', 'обо мне'), ('group', 'наша группа'), ('documents', 'документы'), ('news', 'новости'), ('contacts', 'контакты'), ('awards', 'награды')], default='about', max_length=20, verbose_name='корневое меню'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=50, verbose_name='наименование страницы меню'),
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
