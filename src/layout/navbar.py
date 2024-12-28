import dash_bootstrap_components as dbc
from dash import dcc

navbar = dbc.NavbarSimple(
    brand="Mi Dashboard",
    brand_href="/",
    color="primary",
    dark=True,
    children=[
        dbc.NavItem(dcc.Link("Inicio", href="/", className="nav-link")),
        dbc.NavItem(dcc.Link("Página 1", href="/page-1", className="nav-link")),
        dbc.NavItem(dcc.Link("Página 2", href="/page-2", className="nav-link")),
        dbc.NavItem(dcc.Link("Página 3", href="/page-3", className="nav-link")),
    ],
)
