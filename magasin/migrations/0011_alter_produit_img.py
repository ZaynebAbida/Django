# Generated by Django 5.0.2 on 2024-05-06 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0010_alter_commande_datecde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]