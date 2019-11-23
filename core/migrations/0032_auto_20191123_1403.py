# Generated by Django 2.2.5 on 2019-11-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20191123_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='illegal',
        ),
        migrations.RemoveField(
            model_name='order',
            name='illegal_message',
        ),
        migrations.RemoveField(
            model_name='order',
            name='piece',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
        migrations.AddField(
            model_name='order',
            name='outcome',
            field=models.CharField(choices=[('resolved', 'Resolved'), ('bounced', 'Bounced'), ('illegal', 'Illegal'), ('aux failed', 'Aux failed'), ('aux does not correspond', 'Aux does not correspond')], max_length=25, null=True),
        ),
    ]
