# Generated by Django 4.1.7 on 2023-03-15 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0037_remove_cartbookingmodel_orderstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='img',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
