
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
#Notre équipe component
cards = [
    {
        "src": "assets/Francis_barette-pdg.jpg",
        "header": "Francis Barrette",
        "description": "Président",
        "LinkedIn": "https://www.linkedin.com/in/francis-barrette-32636384/",
        "Facebook": "https://www.facebook.com/francis.barrette.31?mibextid=ZbWKwL",
    },
    {
        "src": "assets/jonathan_valliere.png",
        "header": "Jonathan Vallière",
        "description": "Vice-président",
        "LinkedIn": "https://www.linkedin.com/in/jonathan-valli%C3%A8res-7b32a9235/",
        "Facebook": "https://www.facebook.com/jonathan.vallieres.94?mibextid=ZbWKwL",
    },

]

card_items = []
for card in cards:
    card_item = dbc.Card(
        [
            dbc.CardImg(src=card['src'], top=True, className="card-img-top img-fluid p-3"),
            dbc.CardBody(
                [
                    html.H5(card['header'], className="card-title"),
                    html.P(card['description'], className="card-text"),
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.NavLink(
                                    html.I(className="bi bi-facebook"),
                                    href=card['Facebook'],
                                    target="_blank",
                                    className="social-link",
                                ),
                                width={"size": 2, "order": "first"},
                            ),
                            dbc.Col(
                                dbc.NavLink(
                                    html.I(className="bi bi-linkedin"),
                                    href=card['LinkedIn'],
                                    target="_blank",
                                    className="social-link",
                                ),
                                width={"size": 2, "order": "last"},
                            ),
                        ],
                        className="social-row justify-content-center",
                    ),
                ]
            ),
        ],
        style={"width": "18rem", "margin": "10px"},
        className="team-card text-center mt-5 mb-5 shadow p-3 mb-5 bg-white rounded ",
    )
    card_items.append(card_item)


card_row = dbc.Row(card_items, className="justify-content-center mt-5 mb-5")
