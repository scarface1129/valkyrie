# Generated by Django 3.2.9 on 2022-09-11 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0017_auto_20220911_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadmap',
            name='framework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.framework'),
        ),
    ]