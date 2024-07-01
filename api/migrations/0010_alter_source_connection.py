# Generated by Django 5.0.6 on 2024-07-01 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_source_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='connection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connections', to='api.connection'),
        ),
    ]
