# Generated by Django 4.2 on 2023-04-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0009_additem_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='additem',
            name='p_price',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additem',
            name='s_price',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
