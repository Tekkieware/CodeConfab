# Generated by Django 2.2.6 on 2019-12-26 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CodeConfab', '0014_comment_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
