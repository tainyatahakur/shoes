# Generated by Django 4.1.6 on 2023-03-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_remove_cartbookingmodel_datentime'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartbookingmodel',
            name='datentime',
            field=models.DateField(default='2023-04-04'),
            preserve_default=False,
        ),
    ]
