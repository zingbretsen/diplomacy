# Generated by Django 2.2.10 on 2020-04-23 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200419_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='build_deadline',
            field=models.CharField(choices=[('twelve_hours', '12 hours'), ('twenty_four_hours', '24 hours'), ('two_days', '2 days'), ('three_days', '3 days'), ('five_days', '5 days'), ('seven_days', '7 days')], default='twelve_hours', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='nation_choice_mode',
            field=models.CharField(choices=[('random', 'Random'), ('preference', 'Preference'), ('first_come', 'First come first serve')], default='random', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='order_deadline',
            field=models.CharField(choices=[('twelve_hours', '12 hours'), ('twenty_four_hours', '24 hours'), ('two_days', '2 days'), ('three_days', '3 days'), ('five_days', '5 days'), ('seven_days', '7 days')], default='twenty_four_hours', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='retreat_deadline',
            field=models.CharField(choices=[('twelve_hours', '12 hours'), ('twenty_four_hours', '24 hours'), ('two_days', '2 days'), ('three_days', '3 days'), ('five_days', '5 days'), ('seven_days', '7 days')], default='twenty_four_hours', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='outcome',
            field=models.CharField(blank=True, choices=[('moves', 'Moves'), ('resolved', 'Resolved'), ('bounced', 'Bounced'), ('aux_failed', 'Aux failed'), ('aux_does_not_correspond', 'Aux does not correspond')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='turn',
            name='phase',
            field=models.CharField(choices=[('order', 'Order'), ('retreat_and_disband', 'Retreat and Disband'), ('build', 'Build')], max_length=20),
        ),
    ]