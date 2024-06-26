from django.db import models
from datetime import date 


# Create your models here.

class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.nom + self.adresse + self.email + self.telephone
    def get_queryset(self):
        return Fournisseur.objects.all() # query for all suppliers
    
class Categorie(models.Model):
    TYPE_CHOICES=[('Al','Alimentaire'), ('Mb','Meuble'),('Sn','Sanitaire'), 
    ('Vs','Vaisselle'),('Vt','Vêtement'),('Jx','Jouets'),
    ('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor'),
    ('Imm','Immobilier'),('Para','ParaPharmacie'),
    ('elec','Electroménager'),('Tap','Tapis'),('fr', 'Frais')]

    name= models.CharField(max_length=50,default='Alimentaire', choices=TYPE_CHOICES )

    def __str__(self):
        return self.name
    
class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField(default='Non définie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    TYPE_CHOICES = [('em', 'emballé'), ('fr', 'Frais'), ('cs', 'Conserve')]
    type = models.CharField(max_length=2, default='em', choices=TYPE_CHOICES)
    img=models.ImageField(upload_to='images/',blank=True)
    categorie = models.ForeignKey(Categorie , on_delete=models.CASCADE, null=True)
    Fournisseur=models.ForeignKey(Fournisseur, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return f"{self.libelle} {self.description} {self.prix} {self.type} {self.img} {self.categorie}"
    
class Commande(models.Model):
    dateCde=models.DateField(null=True, default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField(Produit)

    def __str__(self):
        return f"{self.dateCde} {self.totalCde}"
    

class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)




