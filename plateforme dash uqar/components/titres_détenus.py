import pandas as pd 
# Lire les données depuis un fichier Excel
fichier_excel = 'UQAR invest portfolio_2023-03-27.csv'  
feuille = 'UQAR invested portfolio_2023-03'  

# Charger les données dans un DataFrame
df = pd.read_excel(fichier_excel, sheet_name=feuille)