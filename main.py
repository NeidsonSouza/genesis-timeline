import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('genesis_characters.csv')

# Create a new figure
fig, ax = plt.subplots(figsize=(10, 6))

# Initialize a counter for the y-coordinate of bars
y = 0

# Iterate through each row in the DataFrame without sorting
for index, row in df.iterrows():
    name = row['name'].capitalize()
    parenting_age = row['parenting_age']
    lifetime = row['lifetime']

    # Plot the first part of the bar (years until parenting age)
    ax.barh(name, parenting_age, left=y, color='lightblue')
    ax.axvline(
        x=y+lifetime,
        color='red',
        linestyle='--',
        label='Vertical Line',
        linewidth=0.4,
    )

    # Add text inside the bar
    if parenting_age > 0:
        text_x = y + (parenting_age / 2)
        text_y = index
        ax.text(
            text_x,
            text_y,
            f'{parenting_age}',
            ha='center',
            va='center',
            color='black',
            fontsize=10
        )
    if index > 0:
        text_x = y - 10
        text_y = index
        ax.text(
            text_x,
            text_y,
            f'{name}',
            ha='right',
            va='center',
            color='black',
            fontsize=10
        )

    # Plot the second part of the bar (remaining years)
    y += parenting_age
    bar_length = lifetime - parenting_age
    ax.barh(name, bar_length, left=y, color='lightgreen')

    # Add text inside the bar
    text_x = y + bar_length / 2
    text_y = index
    ax.text(
        text_x,
        text_y,
        f'{bar_length}',
        ha='center',
        va='center',
        color='black',
        fontsize=10
    )

# Set labels and title
ax.set_xlabel('Years Since Creation')
ax.set_ylabel('Characters')
ax.set_title('Genesis Timeline')

# Invert chart
ax.invert_yaxis()

# Display the Gantt chart
plt.tight_layout()
plt.show()
