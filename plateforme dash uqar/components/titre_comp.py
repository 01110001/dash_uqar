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
data = pd.read_csv(csv_file,error_bad_lines=False, sep=';')

# Create a Dash layout

titre =  dbc.Col([
        html.H4("Titre détenus"),
        html.Hr(),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in data.columns],
            data=data.to_dict('records'),
            style_table={
                'overflowX': 'auto',
                'border': '1px solid darkgray',
            },
            style_cell={
                'textAlign': 'left',
                'minWidth': '100px', 'width': '100px', 'maxWidth': '100px',
                'whiteSpace': 'normal',
                'height': 'auto',
                'border': '1px solid darkgray',
                'padding': '5px',
            },
            style_header={
                'fontWeight': 'bold',
                'backgroundColor': 'rgb(230, 230, 230)',
                'border': '1px solid darkgray',
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


