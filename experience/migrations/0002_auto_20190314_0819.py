# Generated by Django 2.1.7 on 2019-03-14 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='begin_date',
            field=models.DateField(verbose_name='дата начала курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='finish_date',
            field=models.DateField(verbose_name='дата завершения курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название курса повышения квалификации'),
        ),
        migrations.AlterField(
            model_name='course',
            name='place',
            field=models.CharField(max_length=100, verbose_name='место проведения курса'),
        ),
    ]
