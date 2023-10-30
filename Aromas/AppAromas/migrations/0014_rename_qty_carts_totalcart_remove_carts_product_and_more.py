# Generated by Django 4.2.5 on 2023-10-29 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAromas', '0013_alter_products_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carts',
            old_name='qty',
            new_name='totalCart',
        ),
        migrations.RemoveField(
            model_name='carts',
            name='product',
        ),
        migrations.AddField(
            model_name='carts',
            name='products',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='code',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='products',
            name='thumbnail',
            field=models.ImageField(blank=True, default='productsImages/error.png', null=True, upload_to='productsImages'),
        ),
        migrations.AlterField(
            model_name='users',
            name='rol',
            field=models.CharField(choices=[('basic', 'Basic'), ('admin', 'Admin'), ('staff', 'Staff')], default='basic', max_length=5),
        ),
    ]
