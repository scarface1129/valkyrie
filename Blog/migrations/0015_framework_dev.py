# Generated by Django 3.2.9 on 2022-09-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_rename_category_framework_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='framework',
            name='dev',
            field=models.CharField(blank=True, choices=[('front', 'Front-End'), ('back', 'Back-End')], max_length=40, null=True),
        ),
    ]