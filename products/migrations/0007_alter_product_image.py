# Generated by Django 4.2.5 on 2023-09-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_alter_product_image_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/images/no_image.png', upload_to='products/media/'),
        ),
    ]
