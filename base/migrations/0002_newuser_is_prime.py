# Generated by Django 3.2.9 on 2021-11-26 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='is_prime',
            field=models.BooleanField(default=False),
        ),
    ]
