# Generated by Django 4.0.3 on 2022-03-08 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0001_initial'),
        ('drone', '0002_alter_drone_medications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='medications',
            field=models.ManyToManyField(blank=True, through='drone.LoadingDrone', to='medication.medication'),
        ),
    ]
