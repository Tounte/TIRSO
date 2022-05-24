from django.shortcuts import render
from etat_stock.models import Livraison, Reception, Avaries
from etat_stock.models import Etat_Stock 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



@login_required(login_url='login')
def stock(request):
    etat_stock_list=Etat_Stock.objects.all()
    return render(request,"etat_stock.html",{"stocks":etat_stock_list})

@login_required(login_url='login')
def reception(request):
    reception_list=Reception.objects.all()
    return render(request,"reception.html",{"reception":reception_list})

@login_required(login_url='login')
def livraison(request):
    livraison_list=Livraison.objects.all()
    return render(request,"livraison.html",{"livraison":livraison_list})

@login_required(login_url='login')
def avaries(request):
    avaries_list=Avaries.objects.all()
    return render(request,"avaries.html",{"avaries":avaries_list})


