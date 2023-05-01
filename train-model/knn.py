import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html

# load the data
df = pd.read_csv("../initial_dataset/employee_working_hours.csv")

# create the dropdown options for employee names
employee_options = [{'label': name, 'value': name}
                    for name in df['employee_name'].unique()]

# create the Dash app
app = dash.Dash(__name__)

# define the layout of the app
app.layout = html.Div([
    html.H1("Working Hours by Date"),
    html.Label("Select Employee:"),
    dcc.Dropdown(
        id='employee-dropdown',
        options=employee_options,
        value=df['employee_name'].unique()[0]
    ),
    dcc.Graph(id='working-hours-graph')
])

# define the callback function for the graph


@app.callback(
    dash.dependencies.Output('working-hours-graph', 'figure'),
    [dash.dependencies.Input('employee-dropdown', 'value')])
def update_figure(selected_employee):
    # filter the data by the selected employee
    filtered_df = df[df['employee_name'] == selected_employee]

    # group the data by date and calculate the total working hours per date
    groupby_date = filtered_df.groupby(
        'date')['hours_of_work'].sum().reset_index()

    # create the graph
    fig = px.line(groupby_date, x='date', y='hours_of_work',
                  title=f"Working Hours for {selected_employee}")
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Working Hours')
    return fig


# run the app
if __name__ == '__main__':
    app.run_server(debug=True)
