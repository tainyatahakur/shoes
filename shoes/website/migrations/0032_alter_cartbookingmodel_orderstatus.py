# Generated by Django 4.1.6 on 2023-03-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0031_customuser_dod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartbookingmodel',
            name='OrderStatus',
            field=models.CharField(max_length=15),
        ),
    ]
