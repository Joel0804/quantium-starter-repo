import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# Load your cleaned CSV file
df = pd.read_csv("formatted_sales_data.csv")  # Change path if needed

# Ensure 'date' is datetime and data is sorted
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create Dash app
app = Dash(__name__)
app.title = "Sales Dashboard"

# App layout
app.layout = html.Div(style={'fontFamily': 'Arial', 'padding': '30px'}, children=[
    html.H1("🛍️ Pink Morsel Sales Dashboard", style={'textAlign': 'center'}),
    
    html.P("This line chart visualizes the sales of Pink Morsels over time across all regions.",
           style={'textAlign': 'center', 'fontSize': '18px', 'marginBottom': '40px'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(df, x='date', y='sales', 
                       title='Sales Over Time',
                       labels={'date': 'Date', 'sales': 'Sales ($)'},
                       template='plotly_white')
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
