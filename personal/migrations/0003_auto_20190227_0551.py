# Generated by Django 2.1.7 on 2019-02-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20190222_1654'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paragraph',
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'секция', 'verbose_name_plural': 'секции'},
        ),
        migrations.AddField(
            model_name='section',
            name='enable',
            field=models.BooleanField(default=1, verbose_name='активность секции'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='section',
            table='sections',
        ),
    ]