# Generated by Django 5.0.2 on 2024-02-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_categorie_produit_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('Al', 'Alimentaire'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'), ('Vt', 'Vêtement'), ('Jx', 'Jouets'), ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor'), ('Imm', 'Immobilier'), ('Para', 'ParaPharmacie'), ('elec', 'Electroménager'), ('Tap', 'Tapis'), ('fr', 'Frais')], default='Alimentaire', max_length=50),
        ),
    ]
