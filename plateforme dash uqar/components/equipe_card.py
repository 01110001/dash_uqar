
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
#Notre équipe component
cards = [
    {
        "src": "https://via.placeholder.com/300x150",
        "header": "John Doe",
        "description": "Software Engineer"
    },
    {
        "src": "https://via.placeholder.com/300x150",
        "header": "Jane Doe",
        "description": "Data Scientist"
    },
    {
        "src": "https://via.placeholder.com/300x150",
        "header": "Bob Smith",
        "description": "Project Manager"
    }
]

card_items = []
for card in cards:
    card_item = dbc.Card(
        [
            dbc.CardImg(src=card['src'], top=True),
            dbc.CardBody(
                [
                    html.H5(card['header'], className="card-title"),
                    html.P(card['description'], className="card-text"),
                ]
            ),
        ],
        style={"width": "18rem", "margin": "10px"},
    )
    card_items.append(card_item)

card_row = dbc.Row(card_items, className="justify-content-center mt-5 mb-5")
