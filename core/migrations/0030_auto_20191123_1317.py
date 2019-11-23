# Generated by Django 2.2.5 on 2019-11-23 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20191123_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piece',
            name='active',
        ),
        migrations.RemoveField(
            model_name='piece',
            name='dislodged_state',
        ),
        migrations.RemoveField(
            model_name='piece',
            name='nation',
        ),
        migrations.RemoveField(
            model_name='piece',
            name='turn',
        ),
        migrations.AddField(
            model_name='piece',
            name='nation_state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pieces', to='core.NationState'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='piece',
            name='dislodged_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='piece_disloged', to='core.Piece'),
        ),
    ]