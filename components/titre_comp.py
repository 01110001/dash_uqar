import pandas as pd
import requests
from io import StringIO
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
import time

# Replace this with your Google Drive file's ID
file_id = "1TWd1pJQAfuxVn5_cws7zqlQmOKjb-5A8"
file_id_2 = "168QPRnI-A-qXX-f682xVPyERM79aO1Fy" # this is the file id for the second file named performance portefeuille
# Construct the download URL
url = f"https://drive.google.com/uc?export=download&id={file_id}"
url_2 = f"https://drive.google.com/uc?export=download&id={file_id_2}"

response = requests.get(url)
time.sleep(5)  # Add a delay of 5 seconds to avoid being caught as a bot
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



#sum of the valeur marchande
total_valeur_marchande = data['Valeur_marchande'].sum()
total_liquidité = data.loc[data['Entreprise'] == 'Canadian Dollar', 'Valeur_marchande'].sum()
#sum of ponderation by secteur
total_ponderation = data.groupby('Secteur')['Ponderation'].sum()

# ajout d'une colonne de rendement
data['Rendement'] = ((data['prix_actuelle'] - data['prix_achat']) / data['prix_achat'] * 100).round(3)

#distribution des entreprises par secteur
grouped_sector=data.groupby('Secteur')['Entreprise'].count()

# Create a Dash layout

def generate_sector_table(data, sector):
    sector_data = data[data['Secteur'] == sector]

    return html.Div([
        html.H4(f"Secteur: {sector}", style={"margin": "15px"}),
        html.Hr(),
        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in sector_data.columns],
            data=sector_data.to_dict('records'),
             style_cell={
                'textAlign': 'center',
                'padding': '10px',
                'maxWidth': '50%',
                'whiteSpace': 'normal',
                'font-family': 'Helvetica',
                'fontSize': 14,
            },
            style_header={
                'fontWeight': 'bold',
                'textAlign': 'center',
                'backgroundColor': '#f7f7f7',
                'border': '1px solid black',
                'font-family': 'Helvetica',
                'fontSize': 12,
            },
            style_data_conditional=[
                {'if': {'row_index': 'odd'}, 'backgroundColor': '#f7f7f7'},
                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'},
            ],
            style_table={
                'maxWidth': '100%',
                'align': 'center',
                'border': 'thin lightgrey solid',
            },
            sort_action='native',
            page_action='native',
            page_current=0,
        ), 
    ], style={'marginBottom': '30px', 'marginTop': '30px'})


sectors = data['Secteur'].unique()



sectors_layout = html.Div([
    html.Div([
        html.H1("Résumé des titre détenus", style={'text-align': 'center', 'padding': '20px', 'color': '#4a4a4a'}),
    ], style={'backgroundColor': '#ffffff', 'borderBottom': '3px solid #4a4a4a', 'marginBottom': '30px'}),

    html.Div([
        html.Div([generate_sector_table(data, sector) for sector in sectors],
                 style={'display': 'flex', 'flexWrap': 'wrap', 'marginBottom': '30px'})
    ]),
], style={'font-family': 'Helvetica', 'margin': '0 auto', 'width': '80%'})








