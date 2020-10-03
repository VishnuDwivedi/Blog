# Generated by Django 2.2.4 on 2019-11-18 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('records', '0005_auto_20191118_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
    ]
