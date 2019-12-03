# Generated by Django 2.1.10 on 2019-11-30 11:10

import cratedb.fields.array
import cratedb.fields.hstore
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0042_auto_20191127_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeterHistory',
            fields=[
                ('meter_history_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('as_of_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='As Of Datetime')),
                ('value', models.FloatField(null=True)),
                ('source', models.CharField(max_length=255)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
                ('created_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Meter')),
                ('uom', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.UnitOfMeasure')),
            ],
            options={
                'db_table': 'core_meter_history',
            },
        ),
    ]