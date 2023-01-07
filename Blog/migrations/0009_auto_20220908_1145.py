# Generated by Django 3.2.9 on 2022-09-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_framework_road_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='aspect',
            field=models.CharField(blank=True, choices=[('True', 'Coding'), ('False', 'Non-Coding')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]