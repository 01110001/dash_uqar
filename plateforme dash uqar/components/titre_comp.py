import pandas as pd 

data = pd.read_csv("plateforme dash uqar/assets/data.csv")

# Create a Dash layout

titre = dbc.Col([
    html.H4("Titre détenus"),
    html.Hr(),
    dcc.Markdown('''
            ```csv
            {}
            ```
        '''.format(data.to_csv(index=False)))
])

