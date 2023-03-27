
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
# contact form component
contact_form = dbc.Col(
    [
        dbc.Row(
            dbc.Col(
                [
                    html.H2("Contactez-nous"),
                    html.Iframe(
                        src="https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2Ffpuqar&tabs=timeline&width=250&height=70&small_header=false&adapt_container_width=true&hide_cover=false&show_facepile=true&appId",
                        className="d-flex align-items-center justify-content-center mt-3"
                    ),
                    html.P(
                        [
                            "Vous avez des questions?",
                            html.Br(),
                            "N'hésitez pas à nous contacter directement. Nous vous répondrons dans les plus brefs délais."
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Label("Nom", className="form-label"),
                                    dbc.Input(
                                        id ="name-input",
                                        type="text",
                                        placeholder="Entrez votre nom",
                                        className="form-control",
                                        required=True,
                                    ),
                                ],
                                md=6,
                                className="mb-3"
                            ),
                            dbc.Col(
                                [
                                    dbc.Label("Email", className="form-label"),
                                    dbc.Input(
                                        id ="email-input",
                                        type="email",
                                        placeholder="Entrez votre email",
                                        className="form-control",
                                        required=True
                                    ),
                                ],
                                md=6,
                                className="mb-3"
                            ),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Label("Message", className="form-label"),
                                    dbc.Textarea(
                                        id ="message-input",
                                        placeholder="Entrez votre message",
                                        className="form-control",
                                        style={"height": 200}
                                    ),
                                ],
                                className="mb-3"
                            ),
                        ]
                    ),
                    dbc.Button("Envoyer",id ="send-button", color="primary", className="mt-3"),
                ],
                md=10,
            ),
            className="align-items-center justify-content-center d-flex mt-5",
        ),
    ],
    className="mt-5 mb-5 pb-5 pt-5 bg-light rounded-3 shadow-lg p-3 mb-5 bg-body rounded border border-2 align-items-center justify-content-center",

)
