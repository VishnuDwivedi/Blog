# Generated by Django 2.2.4 on 2020-01-21 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0023_auto_20200108_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'default_permissions': 'view'},
        ),
    ]
