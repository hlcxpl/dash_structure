import os

# Definir la estructura de directorios y archivos
project_structure = {
    "src": {
        "app.py": """import dash
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
""",
        "assets": {
            "style.css": """body {
    margin: 0;
    padding: 0;
    overflow-x: hidden;
}

.display-4 {
    font-size: 1.5rem;
}

.nav-link {
    margin: 0.5rem 0;
}""",
            "script.js": "// Archivo JS opcional para scripts personalizados",
            "images": {},  # Carpeta para imágenes
        },
        "layout": {
            "navbar.py": """import dash_bootstrap_components as dbc
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
""",
            "sidebar.py": """from dash import html
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
""",
            "footer.py": "# Archivo para el componente Footer (opcional)",
        },
        "pages": {
            "__init__.py": "",
            "home.py": """from dash import html

layout = html.Div([
    html.H1('Bienvenido a Mi Aplicación Dash'),
    html.P('Esta es la página de inicio.'),
    html.P('Utiliza el menú para navegar a otras páginas.')
])
""",
            "page1.py": """from dash import html

layout = html.Div([
    html.H1('Página 1'),
    html.P('Contenido de la página 1.')
])
""",
            "page2.py": """from dash import html

layout = html.Div([
    html.H1('Página 2'),
    html.P('Contenido de la página 2.')
])
""",
            "page3.py": """from dash import html

layout = html.Div([
    html.H1('Página 3'),
    html.P('Contenido de la página 3.')
])
""",
        },
        "components": {
            "charts.py": "# Archivo para componentes de gráficos",
            "tables.py": "# Archivo para componentes de tablas",
        },
        "data": {
            "dataset.csv": "col1,col2,col3\n1,2,3\n4,5,6\n",  # Ejemplo de archivo de datos
        },
    }
}


# Función para crear directorios y archivos
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)


# Crear la estructura del proyecto
create_structure(".", project_structure)
print("Estructura del proyecto creada con éxito.")
