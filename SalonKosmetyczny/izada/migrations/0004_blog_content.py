# Generated by Django 4.2.1 on 2023-06-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('izada', '0003_delete_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
