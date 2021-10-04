import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Preparing data
trace1 = go.Scatter(x=df['Date'], y=df['Death'], mode='lines', name='Death')
trace2 = go.Scatter(x=df['Date'], y=df['Recovered'], mode='lines', name='Recovered')
trace3 = go.Scatter(x=df['Date'], y=df['Unrecovered'], mode='lines', name='Unrecovered')
data = [trace1,trace2,trace3]


# Preparing layout
layout = go.Layout(title='Weather2014-15 Line chart', xaxis_title="Date",
                   yaxis_title="Number of cases")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')
