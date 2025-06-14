import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

# Load your cleaned CSV file
df = pd.read_csv("formatted_sales_data.csv")

# Convert 'date' to datetime and sort values
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create Dash app
app = Dash(__name__)
app.title = "Sales Dashboard"

# App layout
app.layout = html.Div(style={'fontFamily': 'Arial', 'padding': '30px'}, children=[

    html.H1("🛍️ Pink Morsel Sales Dashboard", style={'textAlign': 'center'}),

    html.P("This line chart visualizes the sales of Pink Morsels over time, with region-based filtering below.",
           style={'textAlign': 'center', 'fontSize': '18px', 'marginBottom': '40px'}),

    html.Div([
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'margin-right': '15px'},
            style={'textAlign': 'center', 'marginBottom': '30px'}
        )
    ]),

    dcc.Graph(id='sales-line-chart')
])

# Callback to update chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region]

    fig = px.line(filtered_df, x='date', y='sales',
                  title=f"Sales Over Time ({selected_region.title()})" if selected_region != 'all' else "Sales Over Time (All Regions)",
                  labels={'date': 'Date', 'sales': 'Sales ($)'},
                  template='plotly_white')
    return fig

# Run app
if __name__ == '__main__':
    app.run(debug=True)
