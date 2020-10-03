# Generated by Django 2.2.4 on 2019-11-18 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_auto_20191112_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetails',
            name='comments',
        ),
        migrations.CreateModel(
            name='BlogComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True)),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.BlogDetails')),
            ],
        ),
    ]
