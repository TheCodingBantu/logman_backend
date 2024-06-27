# Generated by Django 5.0.6 on 2024-06-25 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('api', '0004_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmanuser',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.organization'),
        ),
    ]