# -*- coding: utf-8 -*-
"""
Made in Marseille
@author: Raphael
"""
#email : raphael.attias@laplateforme.io

from forex_python.converter import CurrencyRates, RatesNotAvailableError

def afficher_exemples(exemples):
    print("Exemple de devise : ")
    for code, nom in exemples.items():
        print(f"{code}: {nom}")

def ajouter_devise_personnalisee(conversions_personnalisees):
    devise = input("Entrez la devise personnalisée sous forme de code (ex : EUR pour Euro) : ").upper()
    taux = float(input("Entrez le taux de conversion par rapport à l'USD : "))
    conversions_personnalisees[devise] = taux
    print(f"La devise personnalisée {devise} a été ajoutée avec un taux de {taux} par rapport à l'USD.")

def ajouter_devise_preferee(devise_preferee, conversions_personnalisees):
    devise = input("Entrez le code de la devise préférée : ").upper()
    if devise in conversions_personnalisees:
        devise_preferee.append(devise)
        print(f"La devise {devise} a été ajoutée à vos devises préférées.")
    else:
        print(f"La devise {devise} n'est pas une devise personnalisée. Veuillez l'ajouter d'abord.")

c = CurrencyRates()

# Dictionnaire des exemples de devises avec leurs noms
exemples = {'USD': 'Dollar américain', 'EUR': 'Euro', 'JPY': 'Yen japonais', 'GBP': 'Livre sterling', 'AUD': 'Dollar australien', 'CAD': 'Dollar canadien', 'CHF': 'Franc suisse', 'CNY': 'Yuan chinois', 'SEK': 'Couronne suédoise', 'NZD': 'Dollar néo-zélandais'}

print("Convertisseur de monnaie")

# Afficher les exemples de devises
for code, nom in exemples.items():
    print(f"{code}: {nom}")

# Dictionnaire des taux de conversion personnalisées
conversions_personnalisees = {}

# Liste qui stocke les devises préférées de l'utilisateur
devise_preferee = []

#Le menu
print("Convertisseur de monnaie")
while True:
    print("\nOptions : ")
    print("1. Afficher les exemples de devise")
    print("2. Ajouter une devise personnalisée")
    print("3. Ajouter une devise préférée")
    print("4. Convertir des devises")
    print("Q. pour quitter")

    choix = input("Choisissez une option (1-4-Q) : ")

    if choix == "1":
        afficher_exemples(exemples)
    elif choix == "2":
        ajouter_devise_personnalisee(conversions_personnalisees)
    elif choix == "3":
        ajouter_devise_preferee(devise_preferee, conversions_personnalisees)
    elif choix == "4":
        devise = input("Entrez une paire de devises (ex : eur usd) : ").split()
        montant = float(input("Entrez le montant à convertir : "))
        # Calcul du change
        try:
            if len(devise) != 2:
                print("Erreur de format (devise1 devise2)")
            else:
                if devise[0].upper() in conversions_personnalisees:
                    rate = conversions_personnalisees[devise[0].upper()]
                else:
                    rate = c.get_rate(devise[0].upper(), devise[1].upper())
                equivalent_montant = montant * rate
                print(f"{montant} {devise[0].upper()} équivaut à {equivalent_montant} {devise[1].upper()}")
        # Message d'erreur
        except RatesNotAvailableError as e:
            print(f"Erreur : Taux de change non disponible actuellement pour {devise[0].upper()} => {devise[1].upper()}, essayez une autre devise.")
    elif choix == "Q" or choix == "q":
        break
    else:
        print("Choix invalide, bien tenté pour la gestion d'erreur ;)")
