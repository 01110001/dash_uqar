import yfinance as yf
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from dash import dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import datetime as dt
import pandas as pd


# Define the stocks you want to fetch data for
tickers = {
    'GAFAM': ['GOOGL', 'AAPL', 'META', 'AMZN', 'MSFT'],
    'Indice' : ['^GSPC', '^IXIC', '^DJI', '^RUT', '^VIX', '^GSPTSE'],
    'Devise' : ['CADUSD=X', 'CADGBP=X', 'CADJPY=X', 'CADNZD=X', 'CADCHF=X', 'CADAUD=X', 'CADEUR=X'],
    'Crypto' : ['BTC-CAD'],
    'Commodité' : ['GC=F','SI=F','CL=F','NG=F' ],
}

custom_names = {
    'GC=F': 'Or',
    'SI=F': 'Argent',
    'CL=F': 'Prétrole',
    'NG=F': 'Gaz naturel',
    '^GSPC': 'S&P 500',
    '^IXIC': 'NASDAQ',
    '^DJI': 'Dow Jones',
    '^RUT': 'Russell 2000',
    '^GSPTSE': 'TSX',
}


def get_returns(tickers_list, start, end):
    data = yf.download(tickers_list, start=start, end=end)['Adj Close']
    return data.pct_change().dropna()

def get_cumulative_returns(returns, periods):
    return ((1 + returns).cumprod() - 1).iloc[-1] * periods

def get_performance_summary(tickers):
    # Flatten tickers dictionary into a list
    tickers_list = []
    for ticker_group in tickers.values():
        tickers_list.extend(ticker_group)

    end_date = dt.date.today()
    start_dates = {
        'Ce mois-ci': end_date - dt.timedelta(days=30),
        '3 Mois': end_date - dt.timedelta(days=90),
        '6 Mois': end_date - dt.timedelta(days=180),
        'YTD': dt.date(end_date.year, 1, 1),
    }

    performance = []

    for label, start_date in start_dates.items():
        returns = get_returns(tickers_list, start_date, end_date)
        periods = (end_date - start_date).days / 365
        cumulative_returns = get_cumulative_returns(returns, periods)
        performance.append(cumulative_returns)

    summary_df = pd.concat(performance, axis=1, keys=start_dates.keys())
    summary_df.index.name = "Ticker"
    summary_df.reset_index(inplace=True)  # Reset index to include 'Ticker' as a column

    return summary_df.round(3)


df = get_performance_summary(tickers)



def generate_table(dataframe, title):
    # Replace tickers with custom names if a mapping exists
    dataframe = dataframe.copy()
    dataframe['Ticker'] = dataframe['Ticker'].apply(lambda x: custom_names.get(x, x))

    return html.Div([
        html.H3(title),
        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in dataframe.columns],
            data=dataframe.to_dict("records"),
            style_cell={
                'textAlign': 'left',
                'padding': '10px',
                'whiteSpace': 'normal',
                'height': 'auto',
                'font-family': 'Helvetica',
                'fontSize': 14,
            },
            style_header={
                'fontWeight': 'bold',
                'textAlign': 'left',
                'backgroundColor': '#f7f7f7',
                'border': '1px solid black',
                'font-family': 'Helvetica',
                'fontSize': 16,
            },
            style_data_conditional=[
                {'if': {'row_index': 'odd'}, 'backgroundColor': '#f7f7f7'},
                {'if': {'row_index': 'even'}, 'backgroundColor': 'white'},
            ],
            style_table={
                'overflowX': 'auto',
                'maxHeight': '500px',
                'overflowY': 'auto',
            },
            style_cell_conditional=[
                {'if': {'column_id': 'Ticker'}, 'fontWeight': 'bold'},
            ],
            sort_action='native',
            page_action='native',
            page_current=0,
        ),
    ])


stock_layout = html.Div([
    html.Div([
        html.H1("Résumé des performances du marché", style={'text-align': 'center', 'padding': '20px', 'color': '#4a4a4a'}),
    ], style={'backgroundColor': '#ffffff', 'borderBottom': '3px solid #4a4a4a', 'marginBottom': '30px'}),

    html.Div([
        html.Div([
            generate_table(df[df['Ticker'].isin(ticker_group)], title)
        ], style={'marginBottom': '30px'})
        for title, ticker_group in tickers.items()
    ]),
], style={'font-family': 'Helvetica', 'margin': '0 auto', 'width': '80%', 'maxWidth': '1200px'})
