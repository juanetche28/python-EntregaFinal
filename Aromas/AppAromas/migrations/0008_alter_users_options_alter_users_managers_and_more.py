# Generated by Django 4.2.5 on 2023-10-19 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppAromas', '0007_alter_users_age'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={},
        ),
        migrations.AlterModelManagers(
            name='users',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
        migrations.RemoveField(
            model_name='users',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='users',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='password',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='users',
            name='username',
        ),
    ]
