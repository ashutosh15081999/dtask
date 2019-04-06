# Generated by Django 2.2 on 2019-04-06 10:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20190406_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='posted_by',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='posted_on',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
