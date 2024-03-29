# Generated by Django 2.2.6 on 2019-11-07 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('notable_use', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Add a link to your resource')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CodeConfab.Language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(verbose_name='Date of birth')),
                ('gender', models.CharField(max_length=6)),
                ('about', models.CharField(blank=True, max_length=200, null=True)),
                ('education', models.CharField(blank=True, max_length=200, null=True, verbose_name='What schools have you attended?')),
                ('religion', models.CharField(blank=True, max_length=20, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('state_of_origin', models.CharField(blank=True, max_length=50, null=True, verbose_name='State of Origin')),
                ('hometown', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('work', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tell us about your work')),
                ('acheivements', models.CharField(blank=True, max_length=200, null=True, verbose_name='Successful work done in programming')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
