# -*- coding: utf-8 -*-
"""
Made in Marseille

@author: Raphael
"""
#programme en-tete programme python
#version python : 
#auteur : ATTAS Raphaël
#email : raphael.attias@laplateforme.io

from forex_python.converter import CurrencyRates, RatesNotAvailableError

c = CurrencyRates()

# Dictionnaire des exemples de devises avec leurs noms
exemples = {'USD': 'Dollar américain', 'EUR': 'Euro', 'JPY': 'Yen japonais', 'GBP': 'Livre sterling', 'AUD': 'Dollar australien', 'CAD': 'Dollar canadien', 'CHF': 'Franc suisse', 'CNY': 'Yuan chinois', 'SEK': 'Couronne suédoise', 'NZD': 'Dollar néo-zélandais'}

print("Convertisseur de monnaie")

# Afficher les exemples de devises
print("Exemples de devises :")
for code, nom in exemples.items():
    print(f"{code}: {nom}")

devise = input("Entrez une paire de devises (ex : eur usd) : ").split()
montant = float(input("Entrez le montant à convertir : "))

try:
    if len(devise) != 2:
        print("Erreur de format (devise1 devise2)")
    else:
        rate = c.get_rate(devise[0].upper(), devise[1].upper())
        equivalent_montant = montant * rate

        print(f"{montant} {devise[0].upper()} équivaut à {equivalent_montant} {devise[1].upper()}")

except RatesNotAvailableError as e:
    print(f"Erreur : Taux de change non disponible pour {devise[0].upper()} => {devise[1].upper()} à la date la plus récente.")
