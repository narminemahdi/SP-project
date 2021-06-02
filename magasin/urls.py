from magasin.forms import FournisseurForm
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [ 
 path('', views.index),
 path('vitrine/', views.vitrine),
 path('formulair/', views.formulair),
 path('acceuil/', views.acceuil),
path('fournisseur/', views.fournisseur),
 path('blog/', views.blog),
 path ('formulairF/' , views.formulairF) , 
 path('commande/',views.commande) , 
path('commandeE/',views.commandeE),
path('ajoutproduit/',views.ajoutproduit),


#url(r'^$', views.mesProduits, name='mesProduits'),
]
