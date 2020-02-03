# Generated by Django 2.2.9 on 2020-02-03 05:34

import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_meter_financials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meterfinancialvalue',
            name='actual_value',
        ),
        migrations.RemoveField(
            model_name='meterfinancialvalue',
            name='model_baseline_value',
        ),
        migrations.RemoveField(
            model_name='meterfinancialvalue',
            name='net_value',
        ),
        migrations.AddField(
            model_name='meterfinancialvalue',
            name='amount',
            field=models.FloatField(null=True, verbose_name='Amount'),
        ),
        migrations.AddField(
            model_name='valuationmethod',
            name='params',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, null=True, verbose_name='Parameters'),
        ),
        migrations.AlterField(
            model_name='meterproduction',
            name='actual_value',
            field=models.FloatField(null=True, verbose_name='Actual Value'),
        ),
        migrations.AlterField(
            model_name='meterproduction',
            name='model_baseline_value',
            field=models.FloatField(null=True, verbose_name='Model Baseline Value'),
        ),
        migrations.DeleteModel(
            name='ValuationMethodPeriod',
        ),
    ]
