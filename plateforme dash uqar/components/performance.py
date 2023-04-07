import plotly.express as px 
import dash_bootstrap_components as dbc
from dash import dcc


from components.titre_comp import (
    data_portefeuille,

)

# Create a Dash layout
fig = px.line(data_portefeuille, x='Date', y='Valeur Portefeuille')
fig.update_traces(line=dict(color='#00AEEF'))
fig.update_layout(title='Valeur Portefeuille Over Time', xaxis_title='Date', yaxis_title='Valeur Portefeuille')
fig.update_xaxes(
    tickformat='%b %Y',
    dtick='M1',
    ticklabelmode='period'
)

fig_layout = dbc.Col([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='valeur-portefeuille-chart',figure=fig),
            width=12
        )
    ],className="team-card text-center mt-5 mb-5 shadow p-3 mb-5 bg-white rounded ")
])
