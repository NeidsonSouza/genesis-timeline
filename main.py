import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('genesis_characters.csv')

# Sort the DataFrame by Lifetime
df.sort_values(by='lifetime', ascending=False, inplace=True)

# Create a new figure
fig, ax = plt.subplots(figsize=(10, 6))

# Initialize a counter for the y-coordinate of bars
y = 0

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    name = row['name']
    parenting_age = row['parenting_age']
    lifetime = row['lifetime']

    # Plot the first part of the bar (years until parenting age)
    ax.barh(name, parenting_age, left=y, color='lightblue')
    y += parenting_age

    # Plot the second part of the bar (remaining years)
    ax.barh(name, lifetime - parenting_age, left=y, color='lightgreen')
    y += lifetime - parenting_age

# Set labels and title
ax.set_xlabel('Years')
ax.set_ylabel('Characters')
ax.set_title('Genesis Characters Gantt Chart')

# Display the Gantt chart
plt.tight_layout()
plt.show()