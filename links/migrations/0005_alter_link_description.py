# Generated by Django 4.1 on 2022-08-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0004_alter_link_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.TextField(blank=True, verbose_name='コメント'),
        ),
    ]
