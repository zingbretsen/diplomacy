# Generated by Django 2.2.5 on 2019-11-23 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20191123_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='process_on_finalized_orders',
            field=models.BooleanField(default=True),
        ),
    ]