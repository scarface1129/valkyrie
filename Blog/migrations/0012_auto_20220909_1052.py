# Generated by Django 3.2.9 on 2022-09-09 09:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0011_auto_20220908_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='category',
        ),
        migrations.AddField(
            model_name='language',
            name='stacks',
            field=models.ManyToManyField(blank=True, related_name='stacks', to=settings.AUTH_USER_MODEL),
        ),
    ]
