# Generated by Django 4.1.6 on 2023-02-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_addtocartmodel_fit'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartbookingmodel',
            name='fit',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='cartbookingmodel',
            name='price',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='cartbookingmodel',
            name='size',
            field=models.JSONField(default=list),
        ),
    ]
