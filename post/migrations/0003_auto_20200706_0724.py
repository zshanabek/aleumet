# Generated by Django 3.0.8 on 2020-07-06 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200704_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
