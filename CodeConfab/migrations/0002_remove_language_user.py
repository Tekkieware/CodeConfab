# Generated by Django 2.2.6 on 2019-11-09 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CodeConfab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='user',
        ),
    ]
