# Generated by Django 2.2.10 on 2020-05-09 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_delete_territorymapdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Variant')),
            ],
        ),
        migrations.CreateModel(
            name='TerritoryMapData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('abbreviation', models.CharField(max_length=100, null=True)),
                ('path', models.TextField()),
                ('text_x', models.FloatField(null=True)),
                ('text_y', models.FloatField(null=True)),
                ('piece_x', models.FloatField(null=True)),
                ('piece_y', models.FloatField(null=True)),
                ('dislodged_piece_x', models.FloatField(null=True)),
                ('dislodged_piece_y', models.FloatField(null=True)),
                ('supply_center_x', models.FloatField(null=True)),
                ('supply_center_y', models.FloatField(null=True)),
                ('map_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='territory_data', to='core.MapData')),
                ('territory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='map_data', to='core.Territory')),
            ],
        ),
    ]
