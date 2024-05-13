from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Categorie, Produit
from .forms import ProduitForm
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .forms import FournisseurForm
from django import  forms
from .models import Fournisseur 
from .forms import UserRegistrationForm
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from rest_framework.views import APIView
from rest_framework.response import Response

from magasin.serializers import CategorySerializer, ProduitSerializer

from rest_framework import viewsets

class ProductViewset(viewsets.ReadOnlyModelViewSet): 
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.filter()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset
    

def index(request):	
    template=loader.get_template('magasin/mesProduits.html')
    list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list})

""" products= Produit.objects.all()
    context={'products':products}
    return render( request,'magasin/mesProduits.html',context )  """

# Create your views here.
def f(request):
    if request.method == "POST" :
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
        else :
            return render(request,'magasin/majProduits.html',{'form':form})
    else:
        form = ProduitForm()
        return render(request,'magasin/majProduits.html',{'form':form})



def fournisseur(request):
    template=loader.get_template('magasin/fournisseur.html')
    object_list=Fournisseur.objects.all()
    return render(request,'magasin/vitrine.html',{'object_list':object_list})



def nouveauFournisseur(request):
    object_list = Fournisseur.objects.all()
    if request.method == 'POST':
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin/nouvFournisseur')
    else:
        form = FournisseurForm()
    return render(request, 'magasin/fournisseur.html', {'form': form , 'object_list': object_list})


def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')

            return redirect('/register')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})


class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    


class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        products = Produit.objects.all()
        serializer = ProduitSerializer(products, many=True)
        return Response(serializer.data)
    



