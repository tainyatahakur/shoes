# Generated by Django 4.1.5 on 2023-02-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_bookingmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
