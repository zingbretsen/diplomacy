# Generated by Django 3.0.6 on 2020-05-23 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200521_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='NamedCoastMapData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=100)),
                ('text_x', models.FloatField(null=True)),
                ('text_y', models.FloatField(null=True)),
                ('piece_x', models.FloatField(null=True)),
                ('piece_y', models.FloatField(null=True)),
                ('dislodged_piece_x', models.FloatField(null=True)),
                ('dislodged_piece_y', models.FloatField(null=True)),
                ('map_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='named_coast_data', to='core.MapData')),
                ('named_coast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_data', to='core.NamedCoast')),
            ],
        ),
    ]
