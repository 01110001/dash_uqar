import plotly.express as px 
import dash_bootstrap_components as dbc
from dash import dcc

from components.titre_comp import (
    total_ponderation,
    grouped_sector,

)


# Create the pie chart
fig = px.pie(data_frame=total_ponderation.reset_index(),
             names='Secteur',
             values='Ponderation',
             title='Ponderation par Secteur')

bar_chart = px.bar(data_frame=grouped_sector.reset_index(),
                   x='Secteur',
                   y='Entreprise',
                   text='Entreprise',
                   title='Distribution des Entreprises par Secteur',
                     color='Secteur',
                      hover_data=['Entreprise']


                   )
                   
bar_chart.update_traces(textposition='outside')
bar_chart.update_layout(
    hovermode="closest",
    plot_bgcolor="white",
    margin=dict(t=40, l=0, r=0, b=0),
    xaxis=dict(
        title="",
        showgrid=True,
        gridcolor="lightgray",
        linecolor="black",
        linewidth=1,
        mirror=True
    ),
    yaxis=dict(
        title="Nombre d'entreprises",
        showgrid=True,
        gridcolor="lightgray",
        linecolor="black",
        linewidth=1,
        mirror=True
    )
)



# Create the layout
fig_layout = dbc.Col([
    dbc.Row([
        dbc.Col(
            dcc.Graph(figure=fig),
            width=12
        )
    ],className="team-card text-center mt-5 mb-5 shadow p-3 mb-5 bg-white rounded "),
    dbc.Row([
        dbc.Col(
            dcc.Graph(figure=bar_chart),
            width=12
        )
    ],className="team-card text-center mt-5 mb-5 shadow p-3 mb-5 bg-white rounded ")
])