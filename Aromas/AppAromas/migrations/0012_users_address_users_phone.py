# Generated by Django 4.2.5 on 2023-10-21 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAromas', '0011_remove_users_picture_carts_user_users_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]