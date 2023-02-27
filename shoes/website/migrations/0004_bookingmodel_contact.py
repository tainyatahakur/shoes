# Generated by Django 4.1.6 on 2023-02-14 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_productmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingmodel',
            name='contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.contactmodel'),
            preserve_default=False,
        ),
    ]