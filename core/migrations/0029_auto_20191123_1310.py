# Generated by Django 2.2.5 on 2019-11-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_nation_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='nationstate',
            name='orders_finalized',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='nationstate',
            name='surrendered',
            field=models.BooleanField(default=False),
        ),
    ]