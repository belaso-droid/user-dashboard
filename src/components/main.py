import os
from datetime import datetime
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

# Load data from CSV file
df = pd.read_csv('data.csv')

# Filter data by date
def filter_data(start_date, end_date):
    filtered_df = df[
        (df['date'] >= start_date) & (df['date'] <= end_date)
    ]
    return filtered_df

# Update layout when dates change
@app.callback(
    Output('graph', 'figure'),
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_graph(start_date, end_date):
    filtered_df = filter_data(start_date, end_date)
    fig = px.bar(filtered_df, x='date', y='value')
    return fig

# Create application layout
app.layout = html.Div([
    html.H1('User Dashboard'),
    dcc.DatePickerRange(
        id='date-picker',
        start_date_placeholder_text='Start date',
        end_date_placeholder_text='End date'
    ),
    dcc.Graph(id='graph')
])

# Run application
if __name__ == '__main__':
    app.run_server(debug=True)