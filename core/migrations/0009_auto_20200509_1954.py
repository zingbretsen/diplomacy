# Generated by Django 2.2.10 on 2020-05-09 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_mapdata_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapdata',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_data', to='core.Variant'),
        ),
    ]
