# Generated by Django 4.2.5 on 2023-09-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='static/imeges/no_image.png', upload_to='media/'),
        ),
    ]
