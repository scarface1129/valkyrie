# Generated by Django 3.2.9 on 2022-05-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='About',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
