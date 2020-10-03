# Generated by Django 2.2.4 on 2019-11-18 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_blogcomments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]