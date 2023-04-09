import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from dash import dcc, html
import dash_bootstrap_components as dbc

# Define the stocks you want to fetch data for
tickers = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA']

# Fetch stock data
data = yf.download(tickers, start='2020-01-01')

# Create a subplot with 3 rows and 2 columns
fig = make_subplots(rows=3, cols=2, subplot_titles=tickers, shared_xaxes=False)

# Loop through each ticker and add a line chart to the subplot
for i, ticker in enumerate(tickers):
    row, col = divmod(i, 2)
    fig.add_trace(go.Scatter(x=data.index,
                             y=data['Close', ticker],
                             mode='lines',
                             name=ticker),
                  row=row + 1, col=col + 1)

# Update the layout
fig.update_layout(title='Stock Prices', showlegend=False, width=1200, height=1200)





# Display the figure
stock_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=fig)
        ])
    ])
])
