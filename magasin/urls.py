from django.urls import include, path
from .views import nouveauFournisseur
from .views import CategoryAPIView , ProduitAPIView

#from django.conf.urls import url
#from .views import index 
from . import views



app_name = 'magasin'

urlpatterns = [ 
     path('', views.index, name='index'),
     path('majProduits/', views.f, name='f'),
     path('nouvFournisseur/', views.nouveauFournisseur, name='nouveauFour'),
     path('register/', views.register, name='register'),
     path('api/category/', CategoryAPIView.as_view()),
     path('api/produits/', ProduitAPIView.as_view()),






]
 
