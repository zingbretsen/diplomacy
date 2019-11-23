# Generated by Django 2.2.5 on 2019-11-23 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20191123_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='nation',
            name='variant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='nations', to='core.Variant'),
            preserve_default=False,
        ),
    ]
