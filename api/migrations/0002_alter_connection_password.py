# Generated by Django 5.0.6 on 2024-06-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='password',
            field=models.BinaryField(),
        ),
    ]
