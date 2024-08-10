# Generated by Django 4.1 on 2024-08-10 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0002_alter_historicalcustomers_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('external_id', models.CharField(max_length=60, unique=True)),
                ('amount', models.FloatField()),
                ('status', models.SmallIntegerField()),
                ('contract_version', models.CharField(max_length=60, unique=True)),
                ('maximum_payment_date', models.DateTimeField(auto_now=True)),
                ('taken_at', models.DateTimeField(auto_now=True)),
                ('outstanding', models.FloatField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customers', verbose_name='Customer')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalLoans',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('external_id', models.CharField(db_index=True, max_length=60)),
                ('amount', models.FloatField()),
                ('status', models.SmallIntegerField()),
                ('contract_version', models.CharField(db_index=True, max_length=60)),
                ('maximum_payment_date', models.DateTimeField(blank=True, editable=False)),
                ('taken_at', models.DateTimeField(blank=True, editable=False)),
                ('outstanding', models.FloatField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('customer_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='customers.customers', verbose_name='Customer')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical loans',
                'verbose_name_plural': 'historical loanss',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
