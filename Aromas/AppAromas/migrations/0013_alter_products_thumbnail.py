# Generated by Django 4.2.5 on 2023-10-22 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAromas', '0012_users_address_users_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='thumbnail',
            field=models.ImageField(default='productsImages/error.png', upload_to='productsImages'),
        ),
    ]
