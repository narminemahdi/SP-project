from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Fournisseur, Produit
from .forms import ProduitForm , FournisseurForm , CommandeForm ,EmballageForm 

from django.shortcuts import redirect


def index(request):
    template=loader.get_template('mesProduits.html')
    list= Produit.objects.all()
    return HttpResponse(template.render( {'list':list} ))
# Create your views here.
def formulair(request):
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else :
        form = ProduitForm() #créer formulaire vide
    return render(request,'majProduits.html',{'form':form})


def formulairF(request):
    if request.method == "POST" : 
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else :
        form = FournisseurForm() #créer formulaire vide
    return render(request,'ajouterF.html',{'form':form}) 
    

def commande(request):
    if request.method == "POST" : 
        form = CommandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else :
        form = CommandeForm() #créer formulaire vide
    return render(request,'commande.html',{'form':form})  


def commandeE(request):
    if request.method == "POST" : 
        form = EmballageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else :
        form = EmballageForm() #créer formulaire vide
    return render(request,'commandeE.html',{'form':form})  


def ajoutproduit(request):
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else :
        form = ProduitForm() #créer formulaire vide
    return render(request,'ajoutProduit.html',{'form':form})  


def vitrine(request):    
    list=Produit.objects.all()
    return render(request,'vitrine.html',{'list':list})

def acceuil(request):    
    return render(request,'acceuil.html' )

def blog(request):    
    return render(request,'blog.html' )

def fournisseur(request):  
    list=Fournisseur.objects.all()  
    return render(request,'fournisseur.html',{'list':list} )

