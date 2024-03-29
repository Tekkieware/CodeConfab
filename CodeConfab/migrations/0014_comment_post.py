# Generated by Django 2.2.6 on 2019-12-21 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CodeConfab', '0013_auto_20191209_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('description', models.TextField(verbose_name='Describe your errors:')),
                ('code', models.TextField(verbose_name='Paste code here:')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Give opinion:')),
                ('code', models.TextField(verbose_name='Paste code if any:')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CodeConfab.Post')),
            ],
        ),
    ]
