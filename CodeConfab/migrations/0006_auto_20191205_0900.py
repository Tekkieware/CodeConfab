# Generated by Django 2.2.6 on 2019-12-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeConfab', '0005_auto_20191205_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
