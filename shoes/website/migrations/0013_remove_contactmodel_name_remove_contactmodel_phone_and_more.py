# Generated by Django 4.1.6 on 2023-02-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_cartbookingmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='phone',
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='city',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='fname',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='lname',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='state',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='username',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='zip',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
    ]
