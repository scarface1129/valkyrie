# Generated by Django 3.2.9 on 2022-09-08 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_blogcategory_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcategory',
            old_name='article',
            new_name='article1',
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='article2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='article3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
