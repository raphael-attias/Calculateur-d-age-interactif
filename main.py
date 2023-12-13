# -*- coding: utf-8 -*-
"""
Made in Marseille

@author: Raphael
"""
#email : raphael.attias@laplateforme.io

from datetime import date
def annee():
    actuel = int(input("Entre l'année actuel : "))
    naissance = int(input("Entre l'année de naissance : "))
    age = actuel - naissance
    print(f"L'âge est de {age} ans")

def age():
    _age = int(input("Entre l'âge : "))
    actuel = int(input("Entre l'année acteul : "))
    naissance = actuel - _age
    print(f"L'année de naissance est: {naissance}")

def annee_mois_jour():
    actuel = date.today()
    naissance_annee = int(input("Entre l'année de naissance : "))
    naissance_mois = int(input("Entre le mois de naissance : "))
    naissance_jour = int(input("Entre le jour de naissance : "))
    naissance = date(naissance_annee, naissance_mois, naissance_jour)
    age_delta = actuel - naissance
    age_annees = age_delta.days // 365
    age_mois = (age_delta.days % 365) // 30
    age_jours = (age_delta.days % 365) % 30  
    print(f"L'âge est de {age_annees} ans, {age_mois} mois, {age_jours} jours")
    return age_delta 

while True:
    print("\nBienvenue dans le calculateur d'âge")
    print("1. Calculer l'âge (année près)")
    print("2. Calculer l'année de naissance")
    print("3. Calculer l'âge (année, mois, jour près)")
    print("q. Quitter")
    choix = input("Choix: ")
    if choix == "1":
        annee()
    elif choix == "2":
        age()
    elif choix == "3":
        annee_mois_jour()
    elif choix == "q":
        break