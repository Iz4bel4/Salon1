# Generated by Django 4.2.1 on 2023-06-16 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('izada', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='blog',
        ),
    ]
