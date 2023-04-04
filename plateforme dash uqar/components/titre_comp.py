import pandas as pd
import requests
from io import StringIO
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table


# Replace this with your Google Drive file's ID
file_id = "1TWd1pJQAfuxVn5_cws7zqlQmOKjb-5A8"

# Construct the download URL
url = f"https://drive.google.com/uc?export=download&id={file_id}"

response = requests.get(url)
response_text = response.text

csv_file = StringIO(response_text)
data = pd.read_csv(csv_file,on_bad_lines='skip',sep=';',encoding='latin-1',decimal=',',thousands='.')

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
    ])


