# Generated by Django 4.0.5 on 2022-07-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0003_walletlistmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletlistmodel',
            name='file',
            field=models.ImageField(upload_to='wallet'),
        ),
    ]
