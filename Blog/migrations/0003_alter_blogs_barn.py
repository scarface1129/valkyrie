# Generated by Django 3.2.9 on 2022-05-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_blogs_barn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='barn',
            field=models.BooleanField(default=False),
        ),
    ]
