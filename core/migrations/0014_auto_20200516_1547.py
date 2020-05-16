# Generated by Django 3.0.6 on 2020-05-16 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20200516_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='turn_created',
            field=models.ForeignKey(blank=True, help_text='The turn during which this piece was created. Will always be a build phase. If null, piece was created at the beginning of the game.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.Turn'),
        ),
    ]
