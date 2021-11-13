# Generated by Django 3.2.9 on 2021-11-12 08:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cart_user',
            field=models.ManyToManyField(related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='wishlist_user',
            field=models.ManyToManyField(related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]