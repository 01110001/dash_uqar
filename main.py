import dash
import datetime as dt
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
import yfinance as yf

from components.sidebar import (
    sidebar,
)

from components.equipe_card import (
    card_row,
)

from components.titre_comp import (
    sectors_layout,

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

from components.Accueil import (
    stock_layout,
)



from Page import (
    contact,
    equipe,
    titre,
    stat,
    performance,
    Accueil,

)



# Create the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP,dbc.icons.FONT_AWESOME], 
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

# Add this line to suppress callback exceptions
app.config.suppress_callback_exceptions = True

server = app.server

app.layout = html.Div([
    dbc.Container(
    dbc.Row(children=[
        dcc.Location(id="url"), 
        dbc.Col(sidebar),
        dbc.Col(id="page-content", width=9),
    ])
)
])





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
    elif pathname == "/":
        return Accueil.create_layout()


@app.callback(
    Output("send-button", "href"),
    Input("name-input", "value"),
    Input("email-input", "value"),
    Input("message-input", "value"),
)
def update_mailto_link(name, email, message):
    if name and email and message:
        mailto_link = f"mailto:?subject=Contact from {name}&body={message}%0A%0AReply to: {email}"
        return mailto_link
    else:
        return ""



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)