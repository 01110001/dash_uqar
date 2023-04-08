import plotly.express as px 
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import calendar
from components.titre_comp import (
    data_portefeuille,

)

# Compute monthly return
data_portefeuille['Month'] = data_portefeuille['Date'].dt.to_period('M')
monthly_returns = data_portefeuille.groupby('Month')['Valeur Portefeuille'].apply(lambda x: x.iloc[-1] / x.iloc[0] - 1).round(3)

# Generate calendar return data
calendar_data = pd.DataFrame({'Date': monthly_returns.index.to_timestamp(), 'Return': monthly_returns.values})
calendar_data['Year'] = calendar_data['Date'].dt.year
calendar_data['Month'] = calendar_data['Date'].dt.month

# Pivot the dataframe to get years as columns and months as index
year_month_return = calendar_data.pivot_table(index='Month', columns='Year', values='Return')

# Map month names to month abbreviations using strftime method
year_month_return.index = year_month_return.index.map(lambda x: calendar.month_abbr[x])

# Add a row for the total returns for each year
year_month_return.loc['Total'] = year_month_return.sum().round(3)

# Convert the index to a column and rename it
year_month_return = year_month_return.reset_index().rename(columns={'index': 'Month'})


# Create the table
table = go.Table(
    header=dict(
        values=list(year_month_return.columns),
        fill_color='gray',
        font=dict(color='white', size=14),
        align='center'
    ),
    cells=dict(
        values=[year_month_return[col] for col in year_month_return.columns],
        fill_color='#F5F8FF',
        font=dict(color='black', size=12),
        align='center'
    )
)

# Create the layout
# Customize the table layout
layout = go.Layout(
    title='Rendement par mois',
    margin=dict(l=20, r=20, t=50, b=20),
)

fig_2 = go.Figure(data=table, layout=layout)


# Create a Dash layout
fig = px.line(data_portefeuille, x='Date', y='Valeur Portefeuille')
fig.update_traces(line=dict(color='#00AEEF'))
fig.update_layout(title='Valeur du Portefeuille dans le temps', xaxis_title='Date', yaxis_title='Valeur Portefeuille',plot_bgcolor='#F9F9F9',paper_bgcolor='#F9F9F9')
fig.update_xaxes(
    tickformat='%b %Y',
    dtick='M1',
    ticklabelmode='period',
    showgrid=False  # Add this line to remove the grid on the x-axis
)
fig.update_yaxes(
    showgrid=False  # Add this line to remove the grid on the y-axis
)

fig_layout = dbc.Col([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='valeur-portefeuille-chart',figure=fig),
            width=12
        )
    ],className="team-card text-center mt-5 mb-5 shadow p-3 mb-5 bg-white rounded "),
        dbc.Row([
        dbc.Col(
            dcc.Graph(id='calendar_dataframe',figure=fig_2),
            width=12
        )
    ],className="team-card text-center mt-5 mb-5 shadow p-3 mb-5 bg-white rounded ")
])
