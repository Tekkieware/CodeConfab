# Generated by Django 2.2.6 on 2020-01-24 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CodeConfab', '0019_auto_20200115_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateField(default=django.utils.timezone.now)),
                ('seen', models.BooleanField(default=False)),
                ('prompted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_prompts', to=settings.AUTH_USER_MODEL)),
                ('prompter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_prompts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sent', models.DateField(default=django.utils.timezone.now)),
                ('seen', models.BooleanField(default=False)),
                ('poked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_pokes', to=settings.AUTH_USER_MODEL)),
                ('poker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_pokes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
