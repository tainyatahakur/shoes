# Generated by Django 4.1.6 on 2023-03-01 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='pass1',
            new_name='password1',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='pass2',
            new_name='password2',
        ),
    ]
