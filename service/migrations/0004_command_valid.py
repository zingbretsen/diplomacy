# Generated by Django 2.1.7 on 2019-07-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20190727_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='valid',
            field=models.BooleanField(default=True),
        ),
    ]