# Generated by Django 4.1 on 2022-08-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_link_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
    ]
