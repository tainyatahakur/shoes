# Generated by Django 4.1.6 on 2023-03-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_cartbookingmodel_orderstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dod',
            field=models.DateField(default='2023-03-03'),
            preserve_default=False,
        ),
    ]
