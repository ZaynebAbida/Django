# Generated by Django 5.0.2 on 2024-02-22 23:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0009_alter_commande_datecde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='dateCde',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
