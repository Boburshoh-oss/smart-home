# Generated by Django 4.0 on 2022-06-29 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_sensorstate_sensor_alter_condition_timer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condition',
            name='sensor_status',
        ),
        migrations.DeleteModel(
            name='SensorState',
        ),
    ]
