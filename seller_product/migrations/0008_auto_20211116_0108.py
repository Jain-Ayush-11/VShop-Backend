# Generated by Django 3.2.9 on 2021-11-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller_product', '0007_auto_20211116_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture2',
            field=models.ImageField(null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture3',
            field=models.ImageField(null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture4',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]