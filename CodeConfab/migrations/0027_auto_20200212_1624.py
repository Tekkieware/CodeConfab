# Generated by Django 2.2.6 on 2020-02-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeConfab', '0026_auto_20200212_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='text',
            field=models.TextField(verbose_name='Reply'),
        ),
    ]
