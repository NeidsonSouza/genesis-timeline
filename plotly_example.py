import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Task': ['Task A', 'Task B', 'Task C', 'Task D', 'Task E', 'Task F', 'Task G', 'Task H', 'Task I', 'Task J'],
    'Start': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-10', '2023-03-01', '2023-03-15', '2023-04-01', '2023-04-15', '2023-05-01', '2023-05-15'],
    'Finish': ['2023-01-10', '2023-01-30', '2023-02-20', '2023-03-05', '2023-03-20', '2023-04-10', '2023-04-30', '2023-05-10', '2023-05-30', '2023-06-15'],
    'Person': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Helen', 'Ivy', 'Jack']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert date columns to datetime format
df['Start'] = pd.to_datetime(df['Start'])
df['Finish'] = pd.to_datetime(df['Finish'])

# Create the Gantt chart
fig = px.timeline(df, x_start='Start', x_end='Finish', y='Person', color='Task', title='Project Timeline Gantt Chart')

# Customize the appearance
fig.update_xaxes(title_text='Timeline')
fig.update_yaxes(categoryorder='total ascending')
fig.update_layout(showlegend=True)

# Show the chart
fig.show()
