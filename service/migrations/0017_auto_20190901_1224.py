# Generated by Django 2.1.7 on 2019-09-01 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0016_auto_20190826_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid', models.BooleanField(default=True)),
                ('success', models.BooleanField(default=True)),
                ('result_message', models.CharField(blank=True, max_length=100, null=True)),
                ('aux_coast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.NamedCoast')),
                ('aux_territory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.Territory')),
                ('order', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.Order')),
                ('source_coast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.NamedCoast')),
                ('source_territory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.Territory')),
                ('target_coast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.NamedCoast')),
                ('target_territory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.Territory')),
            ],
            options={
                'db_table': 'support',
            },
        ),
        migrations.AlterField(
            model_name='move',
            name='order',
            field=models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.Order'),
        ),
        migrations.AlterField(
            model_name='move',
            name='source_territory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.Territory'),
        ),
        migrations.AlterField(
            model_name='move',
            name='target_territory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='service.Territory'),
        ),
    ]