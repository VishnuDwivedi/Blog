# Generated by Django 2.2.4 on 2020-01-08 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0018_commentlikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomments',
            name='likes',
        ),
    ]
