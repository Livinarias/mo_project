# Generated by Django 4.1 on 2024-08-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_alter_historicalloans_contract_version_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalloans',
            name='taken_at',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='loans',
            name='taken_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
