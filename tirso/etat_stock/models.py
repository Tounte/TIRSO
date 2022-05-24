from django.db import models

class Etat_Stock(models.Model):
    caracteres = models.fields.CharField(max_length=100)
    chassis = models.fields.CharField(max_length=100)
    modele = models.fields.CharField(max_length=100)
    boxage = models.fields.CharField(max_length=100)
    immat = models.fields.CharField(max_length=100)
    date = models.fields.DateField(auto_now=True)
    categorie = models.fields.CharField(max_length=100)
    kilometrage = models.fields.CharField(max_length=100)

class Livraison(models.Model):
    caractaires = models.fields.CharField(max_length=100)
    chassis = models.fields.CharField(max_length=100)
    modele = models.fields.CharField(max_length=100)
    destination = models.fields.CharField(max_length=100)
    ville= models.fields.CharField(max_length=100)
    date = models.fields.DateField(auto_now=True)
    heure = models.fields.CharField(max_length=100)
    transport = models.fields.CharField(max_length=100)

class Reception(models.Model):
    caractaires = models.fields.CharField(max_length=100)
    chassis = models.fields.CharField(max_length=100)
    modele = models.fields.CharField(max_length=100)
    origine = models.fields.CharField(max_length=100)
    date = models.fields.DateField(auto_now=True)
    heure = models.fields.CharField(max_length=100)
    transport = models.fields.CharField(max_length=100)

class Avaries(models.Model):
    caractaires = models.fields.CharField(max_length=100)
    chassis = models.fields.CharField(max_length=100)
    box= models.fields.CharField(max_length=100)
    modele = models.fields.CharField(max_length=100)
    date = models.fields.DateField(auto_now=True)
    anomalies = models.fields.TextField(blank=True)
    



class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name
