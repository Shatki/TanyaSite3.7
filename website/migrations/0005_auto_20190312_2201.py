# Generated by Django 2.1.7 on 2019-03-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='наименование страницы')),
                ('template', models.CharField(choices=[('about.html', 'обо мне'), ('documents.html', 'документы'), ('awards.html', 'награды')], default='about.html', max_length=20, verbose_name='страница')),
            ],
            options={
                'verbose_name': 'страница',
                'verbose_name_plural': 'страницы',
                'db_table': 'pages',
            },
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu',
            field=models.CharField(choices=[('about', 'обо мне'), ('group', 'наша группа'), ('docs', 'документы'), ('news', 'новости'), ('contacts', 'контакты'), ('awards', 'награды')], default='about', max_length=20, verbose_name='корневое меню'),
        ),
        migrations.AddField(
            model_name='page',
            name='menu',
            field=models.ForeignKey(on_delete='корневое меню сайта', to='website.Menu'),
        ),
    ]
