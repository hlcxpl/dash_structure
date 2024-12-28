import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from layout.navbar import navbar
from layout.sidebar import sidebar
from pages import home, page1, page2, page3

# Inicializar la aplicación con Bootstrap
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Mi Proyecto Dash'

# Define el layout de la aplicación
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    sidebar,
    html.Div(id='page-content', style={'margin-left': '15%', 'margin-top': '50px', 'padding': '20px'})
])

# Callbacks para el cambio de páginas
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/page-1':
        return page1.layout
    elif pathname == '/page-2':
        return page2.layout
    elif pathname == '/page-3':
        return page3.layout
    else:
        return html.Div([html.H1('404'), html.P('Página no encontrada.')])

if __name__ == '__main__':
    app.run_server(debug=True)
