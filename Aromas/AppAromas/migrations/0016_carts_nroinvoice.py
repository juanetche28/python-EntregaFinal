# Generated by Django 4.2.5 on 2023-10-31 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAromas', '0015_alter_carts_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='nroInvoice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]