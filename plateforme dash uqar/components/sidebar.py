
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
#this function generates an icon and a text for the sidebar
def custom_nav(name, icon):
    """
    Cette fonction génère un icône et un texte pour la sidebar
    name: le nom de l'élément
    icon: l'icône de l'élément en bootstrap
    liens pour icones: https://icons.getbootstrap.com/
    """
    return [
        html.I(className=icon),
        name,
    ]


#sidebar component
sidebar = dbc.Col(
        
    [   
        dbc.Nav(
            [   #add twitter, facebook,linkedin icons here
                html.Img(src="assets/logo.png", style={"width":"235px","height":"180px"}),
                dbc.Col([
                    dbc.NavLink(html.I(className="bi bi-instagram m-2"),href="https://www.instagram.com/fpeuqarlevis/", target="_blank"),
                    dbc.NavLink(html.I(className="bi bi-bank m-2"),href="http://www.fpuqar.ca/", target="_blank"),
                    dbc.NavLink(html.I(className="bi bi-facebook m-2"),href="https://www.facebook.com/fpuqar", target="_blank"),
                    dbc.NavLink(html.I(className="bi bi-linkedin m-2"),href=""),
      ], className="align-items-center justify-content-center d-flex mt-3"),  
                html.Hr(),
                #add custom icon here
                dbc.NavLink(
                    custom_nav("Accueil", "bi bi-house-door-fill me-2"),
                    href="Page/accueil.py", 
                    active="exact", 
                    className="nav-link",
                    ),
                dbc.NavLink(
                    custom_nav("Notre Équipe", "bi bi-people-fill me-2"),
                    href="/equipe", 
                    active="exact", 
                    className="nav-link",
                ),
                dbc.NavLink(
                    custom_nav("Contactez-nous", "bi bi-chat me-2"),
                    href="/contact", 
                    active="exact", 
                    className="nav-link",
                ),
                html.Hr(),
                dbc.NavLink(
                    custom_nav("Performance du fond", "bi bi-graph-up me-2"),
                    href="/performance", 
                    active="exact", 
                    className="nav-link",
                ),
                dbc.NavLink(
                    custom_nav("Statistiques", "bi bi-pie-chart-fill me-2"),
                    href="/stat", 
                    active="exact", 
                    className="nav-link",
                ),
                 dbc.NavLink(
                    custom_nav("Analyse par entreprise", "bi bi-file-earmark-bar-graph me-2"),
                    href="/analyse-par-entreprise", 
                    active="exact", 
                    className="nav-link",
                ),
                dbc.NavLink(
                    custom_nav("Calendrier économique", "bi bi-calendar3 me-2"),
                    href="/calendrier", 
                    active="exact", 
                    className="nav-link",
                ),
                dbc.NavLink(
                    custom_nav("Titres détenus", "bi bi-wallet2 me-2"),
                    href="/Titres-detenus", 
                    active="exact", 
                    className="nav-link",
                    
                    
                ),
                dbc.NavLink(
                    custom_nav("Recheche entreprise", "bi bi-search me-2"),
                    href="/Recheche-entreprise", 
                    active="exact", 
                    className="nav-link",
                ),
            ],
            vertical=True,
            pills=True,
            
        ),
    ], 
    #make this side bar aligned to the left
    className="d-inline-block d-md-block bg-light sidebar ",
)




