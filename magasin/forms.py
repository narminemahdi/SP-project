from django.forms import ModelForm
from .models import Produit , Fournisseur , Commande , Emballage
class ProduitForm(ModelForm): 
    class Meta : 
        model = Produit 
        fields = "__all__" #pour tous les champs de la table

class FournisseurForm(ModelForm): 
    class Meta : 
        model = Fournisseur 
        fields = "__all__"
class CommandeForm(ModelForm): 
    class Meta : 
        model = Commande 
        fields = "__all__"

class EmballageForm(ModelForm): 
    class Meta : 
        model = Emballage 
        fields = "__all__"