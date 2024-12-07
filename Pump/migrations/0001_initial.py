# Generated by Django 5.1.4 on 2024-12-07 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('OFF', 'Off'), ('ON', 'On'), ('ERROR', 'Error')], default='OFF', max_length=10)),
                ('pressure', models.FloatField(default=0.0)),
                ('temperature', models.FloatField(default=0.0)),
                ('performance', models.FloatField(default=0.0)),
                ('power', models.FloatField(default=0.0)),
                ('rotation_speed', models.FloatField(default=0.0)),
                ('is_wheel_rotating', models.BooleanField(default=False)),
                ('valve_status', models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], default='CLOSED', max_length=10)),
            ],
        ),
    ]