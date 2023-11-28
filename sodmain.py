# Import required libraries
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.config.suppress_callback_exceptions = True

# Define the layout of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.Button(id="btn-player-stats", style={
        'background-image': 'url("https://github.com/RasmusNowak/sod/blob/2dc476cdc204bd2da960a4bddb60ab0ede606083/logo%20sod.png?raw=true")',
        'background-size': 'cover',
        'background-position': 'center',  # Ensure the image is centered
        'border-radius': '50%',
        'height': '75px',  # Adjust size as needed
        'width': '75px',   # Adjust size as needed
        'border': 'none',  # Remove border
        'padding': '0',    # Remove padding
        'cursor': 'pointer', # Change cursor on hover
        'outline': 'none', # Remove outline
        'align-items': 'center',
        'justify-content': 'center',
        'display': 'flex',
    }
)
,
html.Button(id="btn-bfd-stats", style={
    'background-image': 'url("https://github.com/RasmusNowak/sod/blob/6c4bf9bfbba1ea6313f4e9b710dd95b4e9b8650d/bfd.png?raw=true")',
    'background-size': 'cover',
    'background-position': 'center',  # Ensure the image is centered
    'border-radius': '50%',
    'height': '75px',  # Adjust size as needed
    'width': '75px',   # Adjust size as needed
    'border': 'none',  # Remove border
    'padding': '0',    # Remove padding
    'cursor': 'pointer', # Change cursor on hover
    'outline': 'none', # Remove outline
    'align-items': 'center',
    'justify-content': 'center',
    'display': 'flex',
}),
html.Button(id="btn-pvp-stats", style={
    'background-image': 'url("https://github.com/RasmusNowak/sod/blob/26a8424e111a00cfad57da4537fbad54eafbed75/pvp%20pic.png?raw=true")',
    'background-size': 'cover',
    'background-position': 'center',  # Ensure the image is centered
    'border-radius': '50%',
    'height': '75px',  # Adjust size as needed
    'width': '75px',   # Adjust size as needed
    'border': 'none',  # Remove border
    'padding': '0',    # Remove padding
    'cursor': 'pointer', # Change cursor on hover
    'outline': 'none', # Remove outline
    'align-items': 'center',
    'justify-content': 'center',
    'display': 'flex',
}),
html.Button(id="btn-talent-stats", style={
    'background-image': 'url("https://cdn.gameleap.com/images/articles/art_EsrorcwPKf/feature/0.75x.webp")',
    'background-size': 'cover',
    'background-position': 'center',  # Ensure the image is centered
    'border-radius': '50%',
    'height': '75px',  # Adjust size as needed
    'width': '75px',   # Adjust size as needed
    'border': 'none',  # Remove border
    'padding': '0',    # Remove padding
    'cursor': 'pointer', # Change cursor on hover
    'outline': 'none', # Remove outline
    'align-items': 'center',
    'justify-content': 'center',
    'display': 'flex',
})
    ], style={'display': 'flex', 'justify-content': 'center', 'background-color': '#000000'}),  # Set the button container background to black
    html.Div(id='page-content')
], style={'background-color': '#000000', 'height': '100vh', 'color': 'white'})  # Set the overall app background to black

# Callbacks to navigate to different pages
@app.callback(Output('url', 'pathname'),
              [Input('btn-player-stats', 'n_clicks'),
               Input('btn-bfd-stats', 'n_clicks'),
               Input('btn-pvp-stats', 'n_clicks'),
               Input('btn-talent-stats', 'n_clicks')],
              prevent_initial_call=True)
def navigate(n1, n2, n3, n4):
    ctx = dash.callback_context

    if not ctx.triggered:
        return '/'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'btn-player-stats':
            return '/player-statistics'
        elif button_id == 'btn-bfd-stats':
            return '/blackfathom-deeps-statistics'
        elif button_id == 'btn-pvp-stats':
            return '/pvp-statistics'
        elif button_id == 'btn-talent-stats':
            return '/talent-statistics'
    raise PreventUpdate

# Function to render each page's content
def render_page_content(pathname):
    if pathname == '/player-statistics':
        # Define layout for Player Statistics
        return html.Div([html.H1('Player Statistics')], style={'backgroundColor': '#000000', 'height': '100vh', 'color': 'white'})
    elif pathname == '/blackfathom-deeps-statistics':
        # Define layout for Blackfathom Deeps Statistics
        return html.Div([html.H1('Blackfathom Deeps Statistics')], style={'backgroundColor': '#000000', 'height': '100vh', 'color': 'white'})
    elif pathname == '/pvp-statistics':
        # Define layout for Player vs Player Statistics
        return html.Div([html.H1('PvP Statistics')], style={'backgroundColor': '#000000', 'height': '100vh', 'color': 'white'})
    elif pathname == '/talent-statistics':
        # Define layout for Talent Statistics
        return html.Div([html.H1('Talent Statistics')], style={'backgroundColor': '#000000', 'height': '100vh', 'color': 'white'})
    else:
        # Default page when no buttons are clicked
        return html.Div([html.H1('Welcome to the WoW Dashboard')], style={'backgroundColor': '#000000', 'height': '100vh', 'color': 'white'})

# Update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return render_page_content(pathname)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
