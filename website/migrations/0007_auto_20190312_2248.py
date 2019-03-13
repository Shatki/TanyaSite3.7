# Generated by Django 2.1.7 on 2019-03-12 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_page_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Menu', verbose_name='корневое меню сайта'),
        ),
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(choices=[('documents.html', 'Шаблон страницы документов'), ('awards.html', 'Шаблон страницы с фотографиями наград')], default='404.html', max_length=20, verbose_name='Шаблон'),
        ),
    ]
