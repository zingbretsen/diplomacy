# Generated by Django 2.2.5 on 2019-11-27 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191124_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nationstate',
            name='turn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nationstates', to='core.Turn'),
        ),
        migrations.AlterField(
            model_name='piece',
            name='turn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pieces', to='core.Turn'),
        ),
        migrations.AlterField(
            model_name='territorystate',
            name='turn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='territorystates', to='core.Turn'),
        ),
    ]
