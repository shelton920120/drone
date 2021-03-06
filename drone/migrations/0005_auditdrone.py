# Generated by Django 3.2.12 on 2022-03-08 20:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0004_rename_battery_drone_battery_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditDrone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('state', models.CharField(choices=[('IDLE', 'IDLE'), ('LOADING', 'LOADING'), ('LOADED', 'LOADED'), ('DELIVERING', 'DELIVERING'), ('DELIVERED', 'DELIVERED'), ('RETURNING', 'RETURNING')], max_length=30, verbose_name='State')),
                ('battery_capacity', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100)])),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.drone')),
            ],
            options={
                'verbose_name': 'AuditDrone',
                'verbose_name_plural': 'AuditDrones',
                'db_table': 'tbl_history_audit_drone',
            },
        ),
    ]
