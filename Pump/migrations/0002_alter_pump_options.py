# Generated by Django 5.1.4 on 2024-12-07 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pump', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pump',
            options={'permissions': [('start_pump', 'Can start the pump'), ('stop_pump', 'Can stop the pump')]},
        ),
    ]