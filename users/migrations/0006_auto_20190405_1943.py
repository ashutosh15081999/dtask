# Generated by Django 2.2 on 2019-04-05 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190405_1942'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='profile',
            index_together={('id', 'slug')},
        ),
    ]
