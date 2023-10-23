# Generated by Django 4.2.5 on 2023-10-19 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppAromas', '0010_alter_avatar_user_alter_users_picture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='picture',
        ),
        migrations.AddField(
            model_name='carts',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='users',
            name='avatar',
            field=models.ImageField(default='avatares/avatar.png', upload_to='avatares'),
        ),
        migrations.AddField(
            model_name='users',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
