from dash import html
import dash_bootstrap_components as dbc

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("Opciones del menú", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Inicio", href="/", active="exact"),
                dbc.NavLink("Página 1", href="/page-1", active="exact"),
                dbc.NavLink("Página 2", href="/page-2", active="exact"),
                dbc.NavLink("Página 3", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={
        "position": "fixed",
        "top": "50px",
        "left": 0,
        "bottom": 0,
        "width": "15%",
        "padding": "20px",
        "background-color": "#f8f9fa",
    },
)
