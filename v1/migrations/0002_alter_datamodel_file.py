# Generated by Django 4.0.5 on 2022-07-05 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamodel',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
