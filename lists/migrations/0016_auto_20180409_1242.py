# Generated by Django 2.0 on 2018-04-09 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0015_auto_20180409_1118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
    ]
