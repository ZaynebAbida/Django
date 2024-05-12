from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required

from magasin.models import Produit
from magasin.serializers import ProduitSerializer

@login_required 


def index(request):
    return render(request,'acceuil.html' )

def acceuil(request):
    context={'val':"Menu Acceuil"}
    return render(request,'acceuil.html',context)


