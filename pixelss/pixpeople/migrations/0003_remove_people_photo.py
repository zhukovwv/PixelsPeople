# Generated by Django 3.2.6 on 2021-08-19 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pixpeople', '0002_auto_20210819_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='photo',
        ),
    ]
