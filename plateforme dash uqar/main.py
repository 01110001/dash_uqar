import dash
import datetime
import pytz
import plotly.figure_factory as ff
from dash import Dash, dcc, html, Input, Output, dash_table
import pandas as pd 
import plotly.express as px 
import dash_bootstrap_components as dbc
import pandas_datareader as pdr
import datetime
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import numpy as np
import calendar
from components.sidebar import (
    sidebar,
)

from components.equipe_card import (
    card_row,
)

from components.titre_comp import (
    titre,

)

from components.stat import (
    fig_layout,

)

from components.performance import (
    fig_layout,

)


from components.contact_form import (
    contact_form,
)




from Page import (
    contact,
    equipe,
    titre,
    Accueil,
    stat,
    performance,

)



# Create the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP,dbc.icons.FONT_AWESOME], 
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])



app.layout = dbc.Container(
    dbc.Row(children=[
        dcc.Location(id="url"), 
        dbc.Col(sidebar),
        dbc.Col(id="page-content", width=9),
    ])
)





# Update page callback
@app.callback(
    Output("page-content", "children"), 
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/contact":
        return contact.create_layout()
    elif pathname == "/equipe":
        return equipe.create_layout()
    elif pathname == "/Titres-detenus":
        return titre.create_layout()
    elif pathname == "/stat":
        return stat.create_layout()
    elif pathname == "/performance":
        return performance.create_layout()







# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)