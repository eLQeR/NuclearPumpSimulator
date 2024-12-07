# Generated by Django 5.1.4 on 2024-12-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('operator', 'Operator'), ('admin', 'Admin'), ('engineer', 'Engineer'), ('viewer', 'Viewer')], default='viewer', max_length=20),
        ),
    ]
