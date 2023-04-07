import pandas as pd
import requests
from io import StringIO
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table

# Replace this with your Google Drive file's ID
file_id = "1TWd1pJQAfuxVn5_cws7zqlQmOKjb-5A8"
file_id_2 = "168QPRnI-A-qXX-f682xVPyERM79aO1Fy" # this is the file id for the second file named performance portefeuille
# Construct the download URL
url = f"https://drive.google.com/uc?export=download&id={file_id}"
url_2 = f"https://drive.google.com/uc?export=download&id={file_id_2}"

response = requests.get(url)
response_2 = requests.get(url_2)
response_text = response.text
response_text_2 = response_2.text

csv_file = StringIO(response_text)
csv_file_2 = StringIO(response_text_2)
data = pd.read_csv(csv_file,on_bad_lines='skip',sep=';',encoding='latin-1',decimal=',',thousands='.')
data_portefeuille = pd.read_csv(csv_file_2,on_bad_lines='skip',sep=';',encoding='latin-1',decimal=',',thousands='.')


# Rename the column and making the date as index
data.columns = ['Symbol', 'Date', 'Entreprise', 'Secteur', 'Ponderation', 'Valeur_marchande', 'prix_achat', 'prix_actuelle']
data_portefeuille.columns = ['Date','rendement','Valeur Portefeuille','dividende','none']
data_portefeuille['Date'] = pd.to_datetime(data_portefeuille['Date'], format= '%d-%m-%Y')
data_portefeuille = data_portefeuille.sort_values(by='Date')
#data_portefeuille.set_index('Date', inplace=True)


#sum of the valeur marchande
total_valeur_marchande = data['Valeur_marchande'].sum()
total_liquidité = data.loc[data['Entreprise'] == 'Canadian Dollar', 'Valeur_marchande'].sum()
#sum of ponderation by secteur
total_ponderation = data.groupby('Secteur')['Ponderation'].sum()

# ajout d'une colonne de rendement
data['Rendement'] = (data['prix_actuelle'] - data['prix_achat']) / data['prix_achat'] * 100

#distribution des entreprises par secteur
grouped_sector=data.groupby('Secteur')['Entreprise'].count()

# Create a Dash layout

titre =  dbc.Col([
        html.H4("Titre détenus", style={"margin": "15px"}),
        html.Hr(),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in data.columns],
            data=data.to_dict('records'),
            style_table={
                'maxHeight': '900px',
                'border': '1px solid darkgray',
            },
            style_cell={
                'textAlign': 'left',
                'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                'whiteSpace': 'normal',
                'height': '100%',
                'border': '1px solid darkgray',
                'padding': '5px',
            },
            style_header={
                'fontWeight': 'bold',
                'backgroundColor': 'rgb(47, 68, 118)',
                'border': '1px solid darkgray',
                'color': 'white',
                'textAlign': 'center',
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)',
                }
            ],
            fixed_rows={'headers': True},
            sort_action="native",
            sort_mode="multi",
            filter_action="native",
            page_action="native",
            page_size=10,
        ),
        html.Hr(),
        html.H4("Total valeur marchande: " + str(total_valeur_marchande) + "$ CAD", style={"margin": "15px"}),
        html.H4("Total liquidité: " + str(total_liquidité) + "$ CAD", style={"margin": "15px"}),
    ])


